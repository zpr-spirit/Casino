<template>
  <div class="home">
    <!-- 顶部标题栏 -->
    <div class="content-header">
      <h1>CSMAR 智能财经报告分析平台</h1>
      <div class="header-actions">
        <el-button type="text">会员套餐</el-button>
        <el-button type="text">在线客服</el-button>
        <el-button type="text">帮助文档</el-button>
      </div>
    </div>
    
    <!-- 主内容 -->
    <div class="content-body">
      <div class="welcome-section">
        <h2>欢迎使用CSMAR智能财经报告分析平台</h2>
        <p>提供专业的股票分析、投资组合管理和量化分析服务</p>
        
        <div class="feature-cards">
          <div class="feature-card" @click="$router.push('/analysis/stock')">
            <el-icon class="feature-icon"><TrendCharts /></el-icon>
            <h3>个股分析</h3>
            <p>深度分析个股基本面和技术面</p>
          </div>
          
          <div class="feature-card" @click="$router.push('/reports')">
            <el-icon class="feature-icon"><Document /></el-icon>
            <h3>我的报告</h3>
            <p>查看和管理您的分析报告</p>
          </div>
          
          <div class="feature-card" @click="$router.push('/quantitative')">
            <el-icon class="feature-icon"><DataAnalysis /></el-icon>
            <h3>量化分析</h3>
            <p>基于数据的量化投资策略</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.home {
  height: 100%;
}

.content-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: white;
  padding: 16px 24px;
  border-bottom: 1px solid #e5e7eb;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.content-header h1 {
  color: #1f2937;
  font-size: 24px;
  font-weight: 600;
}

.header-actions {
  display: flex;
  gap: 16px;
}

.welcome-section {
  text-align: center;
  padding: 60px 20px;
}

.welcome-section h2 {
  color: #1f2937;
  font-size: 32px;
  margin-bottom: 16px;
  font-weight: 600;
}

.welcome-section p {
  color: #6b7280;
  font-size: 18px;
  margin-bottom: 48px;
}

.feature-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  max-width: 900px;
  margin: 0 auto;
}

.feature-card {
  background: white;
  border-radius: 12px;
  padding: 32px 24px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  cursor: pointer;
  transition: all 0.3s;
  border: 1px solid #e5e7eb;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  font-size: 48px;
  color: #1e40af;
  margin-bottom: 16px;
}

.feature-card h3 {
  color: #1f2937;
  font-size: 20px;
  margin-bottom: 12px;
  font-weight: 600;
}

.feature-card p {
  color: #6b7280;
  font-size: 14px;
  line-height: 1.5;
}
</style>
