<template>
  <div class="individual-stock-analysis">
    <!-- 面包屑导航 -->
    <div class="breadcrumb">
      <span>返回首页</span>
      <span class="breadcrumb-separator"> / </span>
      <span>智能分析</span>
      <span class="breadcrumb-separator"> / </span>
      <span>{{ market }}</span>
      <span class="breadcrumb-separator"> / </span>
      <span>个股分析</span>
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
    
    <!-- 个股分析内容 -->
    <div v-if="activeTab === 'individual'" class="analysis-content">
      <!-- 股票搜索 -->
      <div class="search-section">
        <h3 class="section-title">股票搜索分析</h3>
        <div class="search-form">
          <div class="input-group">
            <input 
              v-model="stockInput"
              class="stock-input"
              :placeholder="`请输入${market}股票代码或名称`"
              @keyup.enter="searchStock"
            />
            <button class="search-btn" @click="searchStock" :disabled="!stockInput.trim()">
              <el-icon><Search /></el-icon>
              搜索分析
            </button>
          </div>
        </div>
      </div>
      
      <!-- 搜索结果 -->
      <div v-if="searchResults.length > 0" class="search-results">
        <h4 class="results-title">搜索结果</h4>
        <div class="stock-list">
          <div 
            v-for="stock in searchResults" 
            :key="stock.code"
            class="stock-item"
            @click="selectStock(stock)"
          >
            <div class="stock-info">
              <span class="stock-code">{{ stock.code }}</span>
              <span class="stock-name">{{ stock.name }}</span>
            </div>
            <div class="stock-price">
              <span class="current-price">¥{{ stock.price }}</span>
              <span class="price-change" :class="{ positive: stock.change > 0, negative: stock.change < 0 }">
                {{ stock.change > 0 ? '+' : '' }}{{ stock.change }}%
              </span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 选中股票分析 -->
      <div v-if="selectedStock" class="analysis-section">
        <h4 class="analysis-title">{{ selectedStock.name }} ({{ selectedStock.code }}) 分析报告</h4>
        
        <div class="analysis-tabs">
          <div class="analysis-tab" :class="{ active: analysisType === 'basic' }" @click="analysisType = 'basic'">
            基本信息
          </div>
          <div class="analysis-tab" :class="{ active: analysisType === 'technical' }" @click="analysisType = 'technical'">
            技术分析
          </div>
          <div class="analysis-tab" :class="{ active: analysisType === 'financial' }" @click="analysisType = 'financial'">
            财务分析
          </div>
        </div>
        
        <div class="analysis-content-tab">
          <div v-if="analysisType === 'basic'" class="basic-info">
            <div class="info-grid">
              <div class="info-item">
                <label>股票代码</label>
                <span>{{ selectedStock.code }}</span>
              </div>
              <div class="info-item">
                <label>股票名称</label>
                <span>{{ selectedStock.name }}</span>
              </div>
              <div class="info-item">
                <label>当前价格</label>
                <span class="price">¥{{ selectedStock.price }}</span>
              </div>
              <div class="info-item">
                <label>涨跌幅</label>
                <span :class="{ positive: selectedStock.change > 0, negative: selectedStock.change < 0 }">
                  {{ selectedStock.change > 0 ? '+' : '' }}{{ selectedStock.change }}%
                </span>
              </div>
              <div class="info-item">
                <label>市值</label>
                <span>{{ selectedStock.marketCap }}</span>
              </div>
              <div class="info-item">
                <label>市盈率</label>
                <span>{{ selectedStock.pe }}</span>
              </div>
            </div>
          </div>
          
          <div v-else-if="analysisType === 'technical'" class="technical-analysis">
            <div class="coming-soon">
              <el-icon class="coming-soon-icon"><TrendCharts /></el-icon>
              <h3>技术分析功能开发中...</h3>
              <p>敬请期待更多功能上线</p>
            </div>
          </div>
          
          <div v-else-if="analysisType === 'financial'" class="financial-analysis">
            <div class="coming-soon">
              <el-icon class="coming-soon-icon"><DataAnalysis /></el-icon>
              <h3>财务分析功能开发中...</h3>
              <p>敬请期待更多功能上线</p>
            </div>
          </div>
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
import { ElMessage } from 'element-plus'

export default {
  name: 'IndividualStockAnalysis',
  setup() {
    const route = useRoute()
    const activeTab = ref('individual')
    const stockInput = ref('')
    const searchResults = ref([])
    const selectedStock = ref(null)
    const analysisType = ref('basic')
    
    // 从路由meta获取市场信息
    const market = computed(() => route.meta?.market || 'A股')
    
    // 模拟股票数据
    const mockStocks = [
      { code: '000001', name: '平安银行', price: '12.50', change: 2.35, marketCap: '2,500亿', pe: '8.5' },
      { code: '000002', name: '万科A', price: '18.20', change: -1.25, marketCap: '1,800亿', pe: '12.3' },
      { code: '000858', name: '五粮液', price: '165.80', change: 3.45, marketCap: '6,500亿', pe: '25.8' },
      { code: '600036', name: '招商银行', price: '42.30', change: 1.85, marketCap: '1,200亿', pe: '6.2' },
      { code: '600519', name: '贵州茅台', price: '1,850.00', change: 0.95, marketCap: '23,000亿', pe: '35.6' },
      { code: '000858', name: '五粮液', price: '165.80', change: 3.45, marketCap: '6,500亿', pe: '25.8' },
      { code: '002415', name: '海康威视', price: '35.60', change: -2.15, marketCap: '3,200亿', pe: '18.9' }
    ]
    
    const searchStock = () => {
      if (!stockInput.value.trim()) {
        ElMessage.warning('请输入股票代码或名称')
        return
      }
      
      // 模拟搜索
      const query = stockInput.value.toLowerCase()
      searchResults.value = mockStocks.filter(stock => 
        stock.code.includes(query) || 
        stock.name.toLowerCase().includes(query)
      )
      
      if (searchResults.value.length === 0) {
        ElMessage.info('未找到相关股票')
      }
    }
    
    const selectStock = (stock) => {
      selectedStock.value = stock
      ElMessage.success(`已选择 ${stock.name}`)
    }
    
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
      stockInput,
      searchResults,
      selectedStock,
      analysisType,
      market,
      searchStock,
      selectStock,
      getTabTitle
    }
  }
}
</script>

<style scoped>
.individual-stock-analysis {
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

.analysis-content {
  flex: 1;
  padding: 24px;
  overflow-y: auto;
}

.search-section {
  background: white;
  border-radius: 8px;
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.section-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 16px;
  color: #1f2937;
}

.search-form {
  margin-bottom: 16px;
}

.input-group {
  display: flex;
  gap: 12px;
}

.stock-input {
  flex: 1;
  padding: 12px 16px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.3s;
}

.stock-input:focus {
  border-color: #1e40af;
  box-shadow: 0 0 0 3px rgba(30, 64, 175, 0.1);
}

.search-btn {
  background: linear-gradient(135deg, #7c3aed 0%, #5b21b6 100%);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 8px;
}

.search-btn:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(124, 58, 237, 0.3);
}

.search-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.search-results {
  background: white;
  border-radius: 8px;
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.results-title {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 16px;
  color: #1f2937;
}

.stock-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.stock-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
}

.stock-item:hover {
  background: #f8fafc;
  border-color: #1e40af;
}

.stock-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.stock-code {
  font-weight: 600;
  color: #1f2937;
  font-size: 14px;
}

.stock-name {
  color: #6b7280;
  font-size: 13px;
}

.stock-price {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
}

.current-price {
  font-weight: 600;
  color: #1f2937;
  font-size: 14px;
}

.price-change {
  font-size: 12px;
  font-weight: 500;
}

.price-change.positive {
  color: #10b981;
}

.price-change.negative {
  color: #ef4444;
}

.analysis-section {
  background: white;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.analysis-title {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 20px;
  color: #1f2937;
}

.analysis-tabs {
  display: flex;
  gap: 0;
  margin-bottom: 20px;
  border-bottom: 1px solid #e5e7eb;
}

.analysis-tab {
  padding: 12px 24px;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: all 0.3s;
  font-weight: 500;
  color: #6b7280;
}

.analysis-tab.active {
  color: #1e40af;
  border-bottom-color: #1e40af;
}

.analysis-tab:hover {
  color: #1e40af;
}

.analysis-content-tab {
  min-height: 300px;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.info-item label {
  font-size: 12px;
  color: #6b7280;
  font-weight: 500;
}

.info-item span {
  font-size: 14px;
  color: #1f2937;
  font-weight: 500;
}

.info-item .price {
  color: #1e40af;
  font-weight: 600;
}

.positive {
  color: #10b981;
}

.negative {
  color: #ef4444;
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
}
</style>
