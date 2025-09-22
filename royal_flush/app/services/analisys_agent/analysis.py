"""
Stock Analysis Service
"""
from typing import Optional, List
from datetime import datetime
import random

from app.models.schemas.stock import (
    StockAnalysisRequest,
    StockAnalysisResponse,
    StockSearchRequest,
    StockSearchResponse,
    StockInfo,
    StockAnalysisResult,
    TechnicalAnalysis,
    FundamentalAnalysis,
    RiskAssessment,
    MarketType
)
from app.models.schemas.common import BaseResponse

class StockAnalysisService:
    """Stock analysis service class"""
    
    def __init__(self):
        self.mock_stocks = {
            "000001": {"name": "Ping An Bank", "price": 12.50, "change": 2.35, "market_cap": "250B", "pe": 8.5},
            "000002": {"name": "Vanke A", "price": 18.20, "change": -1.25, "market_cap": "180B", "pe": 12.3},
            "000858": {"name": "Wuliangye", "price": 165.80, "change": 3.45, "market_cap": "650B", "pe": 25.8},
            "600036": {"name": "China Merchants Bank", "price": 42.30, "change": 1.85, "market_cap": "120B", "pe": 6.2},
            "600519": {"name": "Kweichow Moutai", "price": 1850.00, "change": 0.95, "market_cap": "2300B", "pe": 35.6},
            "002415": {"name": "Hikvision", "price": 35.60, "change": -2.15, "market_cap": "320B", "pe": 18.9},
            "300059": {"name": "East Money", "price": 15.80, "change": 1.25, "market_cap": "180B", "pe": 22.5},
            "600031": {"name": "Sany Heavy Industry", "price": 28.90, "change": -0.85, "market_cap": "210B", "pe": 15.8}
        }
    
    async def analyze_stock(self, request: StockAnalysisRequest) -> StockAnalysisResponse:
        """
        Analyze single stock
        
        Args:
            request: Stock analysis request
            
        Returns:
            StockAnalysisResponse: Analysis result
        """
        try:
            # Mock stock data lookup
            stock_data = self.mock_stocks.get(request.stock_code)
            
            if not stock_data:
                return StockAnalysisResponse(
                    success=False,
                    message=f"Stock code {request.stock_code} not found",
                    timestamp=datetime.now().isoformat()
                )
            
            # Build stock basic info
            stock_info = StockInfo(
                code=request.stock_code,
                name=stock_data["name"],
                price=stock_data["price"],
                change_percent=stock_data["change"],
                market_cap=stock_data["market_cap"],
                pe_ratio=stock_data["pe"],
                volume=random.randint(1000000, 10000000),
                turnover=random.uniform(100000000, 1000000000)
            )
            
            # Generate analysis results based on type
            analysis_result = StockAnalysisResult(stock_info=stock_info)
            
            if request.analysis_type in ["technical", "comprehensive"]:
                analysis_result.technical_analysis = self._generate_technical_analysis(stock_data)
            
            if request.analysis_type in ["fundamental", "comprehensive"]:
                analysis_result.fundamental_analysis = self._generate_fundamental_analysis(stock_data)
            
            if request.analysis_type == "comprehensive":
                analysis_result.risk_assessment = self._generate_risk_assessment(stock_data)
                analysis_result.recommendation = self._generate_recommendation(stock_data)
            
            return StockAnalysisResponse(
                success=True,
                message="Stock analysis completed",
                data=analysis_result,
                timestamp=datetime.now().isoformat()
            )
            
        except Exception as e:
            return StockAnalysisResponse(
                success=False,
                message=f"Error during analysis: {str(e)}",
                timestamp=datetime.now().isoformat()
            )
    
    async def search_stocks(self, request: StockSearchRequest) -> StockSearchResponse:
        """
        Search stocks
        
        Args:
            request: Stock search request
            
        Returns:
            StockSearchResponse: Search results
        """
        try:
            results = []
            query_lower = request.query.lower()
            
            for code, data in self.mock_stocks.items():
                if (query_lower in code.lower() or 
                    query_lower in data["name"].lower()):
                    
                    stock_info = StockInfo(
                        code=code,
                        name=data["name"],
                        price=data["price"],
                        change_percent=data["change"],
                        market_cap=data["market_cap"],
                        pe_ratio=data["pe"]
                    )
                    results.append(stock_info)
                    
                    if len(results) >= request.limit:
                        break
            
            return StockSearchResponse(
                success=True,
                message="Search completed",
                data=results,
                count=len(results),
                timestamp=datetime.now().isoformat()
            )
            
        except Exception as e:
            return StockSearchResponse(
                success=False,
                message=f"Error during search: {str(e)}",
                data=[],
                count=0,
                timestamp=datetime.now().isoformat()
            )
    
    async def get_market_stocks(self, market: MarketType) -> dict:
        """
        Get market stock list
        
        Args:
            market: Market type
            
        Returns:
            dict: Stock list
        """
        try:
            stocks = []
            for code, data in self.mock_stocks.items():
                stock_info = StockInfo(
                    code=code,
                    name=data["name"],
                    price=data["price"],
                    change_percent=data["change"],
                    market_cap=data["market_cap"],
                    pe_ratio=data["pe"]
                )
                stocks.append(stock_info)
            
            return {
                "success": True,
                "message": f"Successfully retrieved {market.value} stock list",
                "data": stocks,
                "count": len(stocks),
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Failed to get stock list: {str(e)}",
                "data": [],
                "count": 0,
                "timestamp": datetime.now().isoformat()
            }
    
    def _generate_technical_analysis(self, stock_data: dict) -> TechnicalAnalysis:
        """Generate technical analysis data"""
        return TechnicalAnalysis(
            rsi=round(random.uniform(30, 70), 2),
            macd={
                "macd_line": round(random.uniform(-2, 2), 3),
                "signal_line": round(random.uniform(-2, 2), 3),
                "histogram": round(random.uniform(-1, 1), 3)
            },
            bollinger_bands={
                "upper": round(stock_data["price"] * 1.1, 2),
                "middle": round(stock_data["price"], 2),
                "lower": round(stock_data["price"] * 0.9, 2)
            },
            moving_averages={
                "ma5": round(stock_data["price"] * random.uniform(0.95, 1.05), 2),
                "ma10": round(stock_data["price"] * random.uniform(0.90, 1.10), 2),
                "ma20": round(stock_data["price"] * random.uniform(0.85, 1.15), 2)
            },
            trend=random.choice(["Rising", "Falling", "Sideways"]),
            support_level=round(stock_data["price"] * 0.9, 2),
            resistance_level=round(stock_data["price"] * 1.1, 2)
        )
    
    def _generate_fundamental_analysis(self, stock_data: dict) -> FundamentalAnalysis:
        """Generate fundamental analysis data"""
        return FundamentalAnalysis(
            pe_ratio=stock_data["pe"],
            pb_ratio=round(random.uniform(1.0, 5.0), 2),
            roe=round(random.uniform(5, 25), 2),
            debt_ratio=round(random.uniform(20, 60), 2),
            revenue_growth=round(random.uniform(-10, 30), 2),
            profit_growth=round(random.uniform(-15, 40), 2),
            industry_rank=random.randint(1, 10),
            market_position=random.choice(["Leader", "Second-tier", "Third-tier", "Emerging"])
        )
    
    def _generate_risk_assessment(self, stock_data: dict) -> RiskAssessment:
        """Generate risk assessment data"""
        risk_level = random.choice(["Low Risk", "Medium Risk", "High Risk"])
        return RiskAssessment(
            risk_level=risk_level,
            volatility=round(random.uniform(0.1, 0.5), 3),
            beta=round(random.uniform(0.5, 2.0), 2),
            max_drawdown=round(random.uniform(5, 30), 2),
            var_95=round(random.uniform(2, 10), 2),
            liquidity_risk=random.choice(["Low", "Medium", "High"]),
            credit_risk=random.choice(["Low", "Medium", "High"])
        )
    
    def _generate_recommendation(self, stock_data: dict) -> str:
        """Generate investment recommendation"""
        change = stock_data["change"]
        if change > 3:
            return "Strong Buy"
        elif change > 0:
            return "Buy"
        elif change > -2:
            return "Hold"
        elif change > -5:
            return "Sell"
        else:
            return "Strong Sell"
