<template>
  <div class="quantitative">
    <div class="content-header">
      <h1>量化分析</h1>
    </div>
    
    <div class="content-body">
      <div class="coming-soon">
        <el-icon class="coming-soon-icon"><DataAnalysis /></el-icon>
        <h3>量化分析功能开发中...</h3>
        <p>敬请期待更多功能上线</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Quantitative'
}
</script>

<style scoped>
.quantitative {
  height: 100%;
}

.content-header {
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

.content-body {
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
