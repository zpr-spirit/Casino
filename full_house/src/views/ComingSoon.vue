<template>
  <div class="coming-soon-page">
    <!-- 面包屑导航 -->
    <div class="breadcrumb">
      <span>返回首页</span>
      <span class="breadcrumb-separator"> / </span>
      <span>智能分析</span>
      <span class="breadcrumb-separator"> / </span>
      <span>{{ market }}</span>
    </div>
    
    <!-- 主内容 -->
    <div class="content-body">
      <div class="coming-soon">
        <el-icon class="coming-soon-icon"><TrendCharts /></el-icon>
        <h3>{{ market }}功能开发中...</h3>
        <p>敬请期待更多功能上线</p>
        <div class="feature-preview">
          <h4>即将推出的功能：</h4>
          <ul>
            <li>个股分析</li>
            <li>投资组合管理</li>
            <li>市场感知分析</li>
            <li>实时数据监控</li>
          </ul>
        </div>
        <div class="action-buttons">
          <el-button type="primary" @click="goToAStock">
            查看A股功能
          </el-button>
          <el-button @click="$router.push('/')">
            返回首页
          </el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

export default {
  name: 'ComingSoon',
  setup() {
    const route = useRoute()
    const router = useRouter()
    
    // 从路由meta获取市场信息
    const market = computed(() => route.meta?.market || '港股')
    
    const goToAStock = () => {
      router.push('/analysis/a-stock/individual')
    }
    
    return {
      market,
      goToAStock
    }
  }
}
</script>

<style scoped>
.coming-soon-page {
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
  margin-bottom: 24px;
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

.action-buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
}
</style>
