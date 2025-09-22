#!/usr/bin/env python3
"""
五种技术分析策略可视化演示脚本

这个脚本展示了如何使用StrategyPlotter类来创建包含所有五种策略的综合图表。
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.visualization.strategy_plotter import StrategyPlotter, create_strategy_visualization

def generate_sample_data(days=252):
    """生成示例股票数据"""
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', periods=days, freq='D')
    
    # 模拟价格走势（带趋势和波动）
    trend = np.linspace(100, 120, days)  # 上升趋势
    noise = np.random.normal(0, 2, days)  # 随机噪声
    prices = trend + noise
    
    # 生成OHLC数据
    data = []
    for i, price in enumerate(prices):
        daily_volatility = np.random.uniform(0.5, 2.0)
        high = price + np.random.uniform(0, daily_volatility)
        low = price - np.random.uniform(0, daily_volatility)
        open_price = prices[i-1] if i > 0 else price
        close_price = price
        volume = np.random.randint(1000000, 5000000)
        
        data.append({
            'open': open_price,
            'high': high,
            'low': low,
            'close': close_price,
            'volume': volume
        })
    
    return pd.DataFrame(data, index=dates)

def generate_sample_signals():
    """生成示例策略信号"""
    return {
        'trend_following': {
            'signal': 'bullish',
            'confidence': '75%',
            'metrics': {
                'adx': 35.2,
                'trend_strength': 0.75
            }
        },
        'mean_reversion': {
            'signal': 'neutral',
            'confidence': '60%',
            'metrics': {
                'z_score': 0.8,
                'price_vs_bb': 0.6,
                'rsi_14': 55.3,
                'rsi_28': 52.1
            }
        },
        'momentum': {
            'signal': 'bullish',
            'confidence': '80%',
            'metrics': {
                'momentum_1m': 0.08,
                'momentum_3m': 0.12,
                'momentum_6m': 0.15,
                'volume_momentum': 1.3
            }
        },
        'volatility': {
            'signal': 'neutral',
            'confidence': '55%',
            'metrics': {
                'historical_volatility': 18.5,
                'volatility_regime': 1.1,
                'volatility_z_score': 0.3,
                'atr_ratio': 0.02
            }
        },
        'statistical_arbitrage': {
            'signal': 'bearish',
            'confidence': '45%',
            'metrics': {
                'hurst_exponent': 0.35,
                'skewness': -0.8,
                'kurtosis': 3.2
            }
        },
        'combined_signal': 'bullish'
    }

def main():
    """主函数"""
    print("🚀 开始生成五种技术分析策略可视化图表...")
    
    # 生成示例数据
    print("📊 生成示例股票数据...")
    prices_df = generate_sample_data()
    
    # 生成示例信号
    print("📈 生成示例策略信号...")
    strategy_signals = generate_sample_signals()
    
    # 创建可视化图表
    print("🎨 创建综合可视化图表...")
    try:
        fig = create_strategy_visualization(prices_df, strategy_signals)
        
        # 保存图表
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        chart_filename = f"{output_dir}/five_strategies_analysis.png"
        fig.savefig(chart_filename, dpi=300, bbox_inches='tight')
        plt.close(fig)
        
        print(f"✅ 图表已成功保存至: {chart_filename}")
        print("\n📋 图表包含以下内容:")
        print("   1. 主价格图表 - 价格走势与综合信号")
        print("   2. 趋势跟踪策略 - ADX指标与趋势强度")
        print("   3. 均值回归策略 - Z-Score与RSI")
        print("   4. 动量策略 - 多时间框架动量与成交量")
        print("   5. 波动率策略 - 历史波动率与波动率制度")
        print("   6. 统计套利策略 - Hurst指数与偏度")
        print("   7. 成交量分析 - 成交量与OBV")
        print("   8. 综合信号强度 - 各策略信号对比")
        print("   9. 策略权重分布 - 权重分配饼图")
        print("   10. 历史表现对比 - 各策略置信度")
        print("   11. 风险指标 - 夏普比率、最大回撤、VaR")
        print("   12. 市场状态分析 - 整体市场判断")
        
        # 显示策略信号摘要
        print(f"\n📊 当前策略信号摘要:")
        for strategy, signal_data in strategy_signals.items():
            if strategy != 'combined_signal':
                signal = signal_data['signal']
                confidence = signal_data['confidence']
                print(f"   {strategy}: {signal} ({confidence})")
        
        print(f"\n🎯 综合信号: {strategy_signals['combined_signal']}")
        
    except Exception as e:
        print(f"❌ 生成图表时出错: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
