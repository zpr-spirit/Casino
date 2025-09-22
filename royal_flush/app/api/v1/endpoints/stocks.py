"""
Stock Analysis API Endpoints
"""
from fastapi import APIRouter, HTTPException, Query, Depends
from datetime import datetime, timezone
from typing import Dict
import logging

from app.models.schemas.stock import (
    StockAnalysisRequest,
    StockAnalysisResponse,
    StockSearchRequest,
    StockSearchResponse,
    ApiResponse,
    MarketType
)
from app.models.schemas.common import BaseResponse
from app.services.analisys_agent.analysis import StockAnalysisService
import uuid
from app.state import api_state
from app.services.analisys_agent.analyze_service import execute_stock_analysis
from app.utils.api_utils import serialize_for_api, safe_parse_json
# 延迟导入以避免循环引用
# from src.main import run_hedge_fund


logger = logging.getLogger("analysis_router")
router = APIRouter(prefix="/stocks", tags=["Stock Analysis"])


# Dependency injection
def get_stock_service() -> StockAnalysisService:
    """Get stock analysis service instance"""
    return StockAnalysisService()

@router.post("/analyze", response_model=ApiResponse[StockAnalysisResponse])
async def analyze_stock(
    request: StockAnalysisRequest,
    # service: StockAnalysisService = Depends(get_stock_service)
):
    """
    Analyze single stock
    
    - **stock_code**: Stock code (e.g., 000001)
    - **market**: Market type (a_stock/hk_stock/us_stock)
    - **analysis_type**: Analysis type (basic/technical/fundamental)
    """
    try:
        # result = await service.analyze_stock(request)
        run_id = str(uuid.uuid4())

        # 延迟导入以避免循环引用
        from src.main import run_hedge_fund
        
        # result = run_hedge_fund(
        #     run_id=run_id,
        #     ticker=request.stock_code,
        #     start_date=request.start_date,
        #     end_date=request.end_date,
        #     portfolio={},
        #     show_reasoning=request.show_reasoning,
        #     num_of_news=1,
        # )

        # 将任务提交到线程池
        future = api_state._executor.submit(
            execute_stock_analysis,
            request=request,
            run_id=run_id
        )

        # 注册任务
        api_state.register_analysis_task(run_id, future)

        # 注册运行
        api_state.register_run(run_id)

        # 创建响应对象
        response = StockAnalysisResponse(
            run_id=run_id,
            ticker=request.stock_code,
            status="running",
            message="分析任务已启动",
            submitted_at=datetime.now(timezone.utc)
        )

        # 使用ApiResponse包装返回
        return ApiResponse(
            success=True,
            message="分析任务已完成",
            data={"result": response}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{run_id}/status", response_model=ApiResponse[Dict])
async def get_analysis_status(run_id: str):
    task = api_state.get_analysis_task(run_id)
    run_info = api_state.get_run(run_id)

    if not run_info:
        return ApiResponse(
            success=False,
            message=f"分析任务 '{run_id}' 不存在",
            data=None
        )

    status_data = {
        "run_id": run_id,
        "status": run_info.status,
        "start_time": run_info.start_time,
        "end_time": run_info.end_time,
    }

    if task:
        if task.done():
            if task.exception():
                status_data["error"] = str(task.exception())
            status_data["is_complete"] = True
        else:
            status_data["is_complete"] = False

    return ApiResponse(data=status_data)


@router.get("/{run_id}/result", response_model=ApiResponse[Dict])
async def get_analysis_result(run_id: str):
    try:
        task = api_state.get_analysis_task(run_id)
        run_info = api_state.get_run(run_id)

        if not run_info:
            return ApiResponse(
                success=False,
                message=f"分析任务 '{run_id}' 不存在",
                data=None
            )

        # 检查任务是否完成
        if run_info.status != "completed":
            return ApiResponse(
                success=False,
                message=f"分析任务尚未完成或已失败，当前状态: {run_info.status}",
                data={"status": run_info.status}
            )

        # 收集所有参与此运行的Agent数据
        agent_results = {}
        ticker = ""
        for agent_name in run_info.agents:
            agent_data = api_state.get_agent_data(agent_name)
            if agent_data and "reasoning" in agent_data:
                # 尝试解析和序列化推理数据
                reasoning_data = safe_parse_json(agent_data["reasoning"])
                agent_results[agent_name] = serialize_for_api(reasoning_data)

            # 尝试从market_data_agent获取ticker
            if agent_name == "market_data" and agent_data and "output_state" in agent_data:
                try:
                    output = agent_data["output_state"]
                    if "data" in output and "ticker" in output["data"]:
                        ticker = output["data"]["ticker"]
                except Exception:
                    pass

        # 尝试获取portfolio_management的最终决策
        final_decision = None
        portfolio_data = api_state.get_agent_data("portfolio_management")
        if portfolio_data and "output_state" in portfolio_data:
            try:
                output = portfolio_data["output_state"]
                messages = output.get("messages", [])
                # 获取最后一个消息
                if messages:
                    last_message = messages[-1]
                    if hasattr(last_message, "content"):
                        # 尝试解析content，可能是JSON字符串
                        final_decision = safe_parse_json(last_message.content)
            except Exception as e:
                logger.error(f"解析最终决策时出错: {str(e)}")

        result_data = {
            "run_id": run_id,
            "ticker": ticker,
            "completion_time": run_info.end_time,
            "final_decision": serialize_for_api(final_decision),
            "agent_results": agent_results
        }

        return ApiResponse(data=result_data)
    except Exception as e:
        logger.error(f"获取分析结果时出错: {str(e)}")
        return ApiResponse(
            success=False,
            message=f"获取分析结果时出错: {str(e)}",
            data={"error": str(e)}
        )


@router.get("/search", response_model=StockSearchResponse)
async def search_stocks(
    query: str = Query(..., description="Search keyword", example="Ping An"),
    market: MarketType = Query(..., description="Market type", example="a_stock"),
    limit: int = Query(default=10, description="Return limit"),
    service: StockAnalysisService = Depends(get_stock_service)
):
    """
    Search stocks
    
    - **query**: Search keyword (stock code or name)
    - **market**: Market type
    - **limit**: Return limit
    """
    try:
        search_request = StockSearchRequest(
            query=query,
            market=market,
            limit=limit
        )
        result = await service.search_stocks(search_request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/market/{market}/list")
async def get_market_stocks(
    market: MarketType,
    service: StockAnalysisService = Depends(get_stock_service)
):
    """
    Get market stock list
    
    - **market**: Market type
    """
    try:
        result = await service.get_market_stocks(market)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health", response_model=BaseResponse)
async def health_check():
    """Health check endpoint"""
    return BaseResponse(
        success=True,
        message="Stock analysis service running normally",
        timestamp=datetime.now().isoformat()
    )
