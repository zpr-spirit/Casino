<template>
  <div class="portfolio-analysis">
    <!-- 面包屑导航 -->
    <div class="breadcrumb">
      <span>返回首页</span>
      <span class="breadcrumb-separator"> / </span>
      <span>智能分析</span>
      <span class="breadcrumb-separator"> / </span>
      <span>{{ market }}</span>
      <span class="breadcrumb-separator"> / </span>
      <span>投资组合</span>
    </div>
    
    <!-- 标签页 -->
    <div class="tabs-container">
      <div class="tab-item" :class="{ active: activeTab === 'individual' }" @click="activeTab = 'individual'">
        个股分析
      </div>
      <div class="tab-item" :class="{ active: activeTab === 'portfolio' }" @click="activeTab = 'portfolio'">
        投资组合
      </div>
      <div class="tab-item" :class="{ active: activeTab === 'market' }" @click="activeTab = 'market'">
        市场感知
      </div>
    </div>
    
    <!-- 投资组合内容 -->
    <div v-if="activeTab === 'portfolio'" class="portfolio-content">
      <div class="coming-soon">
        <el-icon class="coming-soon-icon"><TrendCharts /></el-icon>
        <h3>投资组合功能开发中...</h3>
        <p>敬请期待更多功能上线</p>
        <div class="feature-preview">
          <h4>即将推出的功能：</h4>
          <ul>
            <li>多股票组合分析</li>
            <li>风险收益评估</li>
            <li>组合优化建议</li>
            <li>历史回测分析</li>
          </ul>
        </div>
      </div>
    </div>
    
    <!-- 其他标签页内容 -->
    <div v-else class="tab-content">
      <div class="coming-soon">
        <el-icon class="coming-soon-icon"><Clock /></el-icon>
        <h3>{{ getTabTitle(activeTab) }}功能开发中...</h3>
        <p>敬请期待更多功能上线</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'

export default {
  name: 'PortfolioAnalysis',
  setup() {
    const route = useRoute()
    const activeTab = ref('portfolio')
    
    // 从路由meta获取市场信息
    const market = computed(() => route.meta?.market || 'A股')
    
    const getTabTitle = (tab) => {
      const titles = {
        individual: '个股分析',
        portfolio: '投资组合',
        market: '市场感知'
      }
      return titles[tab] || tab
    }
    
    return {
      activeTab,
      market,
      getTabTitle
    }
  }
}
</script>

<style scoped>
.portfolio-analysis {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.breadcrumb {
  padding: 16px 24px;
  background: white;
  border-bottom: 1px solid #e5e7eb;
  font-size: 14px;
  color: #6b7280;
}


.breadcrumb-separator {
  margin: 0 8px;
  color: #9ca3af;
}

.tabs-container {
  padding: 0 24px;
  background: white;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  gap: 0;
}

.tab-item {
  display: inline-block;
  padding: 16px 24px;
  cursor: pointer;
  border-bottom: 3px solid transparent;
  transition: all 0.3s;
  font-weight: 500;
  color: #6b7280;
}

.tab-item.active {
  color: #1e40af;
  border-bottom-color: #1e40af;
}

.tab-item:hover {
  color: #1e40af;
}

.portfolio-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.tab-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.coming-soon {
  text-align: center;
  color: #6b7280;
  max-width: 600px;
}

.coming-soon-icon {
  font-size: 64px;
  margin-bottom: 16px;
  color: #d1d5db;
}

.coming-soon h3 {
  font-size: 24px;
  margin-bottom: 8px;
  color: #374151;
}

.coming-soon p {
  font-size: 16px;
  margin-bottom: 24px;
}

.feature-preview {
  background: #f8fafc;
  border-radius: 8px;
  padding: 24px;
  text-align: left;
  margin-top: 24px;
}

.feature-preview h4 {
  color: #1f2937;
  font-size: 16px;
  margin-bottom: 12px;
  font-weight: 600;
}

.feature-preview ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.feature-preview li {
  padding: 8px 0;
  color: #6b7280;
  position: relative;
  padding-left: 20px;
}

.feature-preview li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #10b981;
  font-weight: bold;
}
</style>
