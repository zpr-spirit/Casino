import logging
from typing import Dict, Any
from datetime import datetime, timezone

from app.models.schemas.stock import StockAnalysisRequest
from app.utils.context_managers import workflow_run
from app.state import api_state
from app.schemas import AgentExecutionLog

logger = logging.getLogger("analysis_service")


def execute_stock_analysis(request: StockAnalysisRequest, run_id: str) -> Dict[str, Any]:
    from src.main import run_hedge_fund  # 避免循环导入

    try:

        # # 初始化投资组合
        # portfolio = {
        #     "cash": request.initial_capital,
        #     "stock": request.initial_position
        # }

        # 执行分析 - 让系统自动计算日期
        logger.info(f"开始执行股票 {request.stock_code} 的分析任务 (运行ID: {run_id})")

        # 创建主工作流日志记录
        workflow_log = AgentExecutionLog(
            agent_name="workflow_manager",
            run_id=run_id,
            timestamp_start=datetime.now(timezone.utc),
            timestamp_end=datetime.now(timezone.utc),  # 初始化为相同值，稍后更新
            input_state={"request": request.dict()},
            output_state=None  # 稍后更新
        )

        # 还不添加到存储，等待工作流完成后再更新

        with workflow_run(run_id):
            result = run_hedge_fund(
                run_id=run_id,
                ticker=request.stock_code,
                start_date=request.start_date,
                end_date=request.end_date,
                portfolio={},
                show_reasoning=request.show_reasoning,
                num_of_news=1,
            )

            # 更新工作流日志的结束时间和输出状态
            # workflow_log.timestamp_end = datetime.now(UTC)
            # workflow_log.output_state = result

            # 添加到日志存储
            # log_storage.add_agent_log(workflow_log)

        logger.info(f"股票分析任务完成 (运行ID: {run_id})")
        return result
    except Exception as e:
        logger.error(f"股票分析任务失败: {str(e)}")

        # 在出错时也记录日志
        # try:
        #     workflow_log.timestamp_end = datetime.now(UTC)
        #     workflow_log.output_state = {"error": str(e)}
        #     log_storage.add_agent_log(workflow_log)
        # except Exception as log_err:
        #     logger.error(f"记录错误日志时发生异常: {str(log_err)}")

        # 更新运行状态为错误
        api_state.complete_run(run_id, "error")
        raise
