<template>
  <div class="sidebar">
    <!-- 菜单项 -->
    <div class="sidebar-menu">
      <div 
        class="menu-item" 
        :class="{ active: $route.path === '/' }"
        @click="$router.push('/')"
      >
        <el-icon class="menu-icon"><House /></el-icon>
        首页
      </div>
      
      <div 
        class="menu-item" 
        :class="{ active: $route.path.startsWith('/analysis') }"
        @click="toggleAnalysisMenu"
      >
        <el-icon class="menu-icon"><TrendCharts /></el-icon>
        智能分析
        <el-icon class="menu-icon" style="margin-left: auto;">
          <ArrowDown v-if="analysisMenuOpen" />
          <ArrowRight v-else />
        </el-icon>
      </div>
      
      <!-- 智能分析子菜单 -->
      <div v-show="analysisMenuOpen" class="submenu">
        <!-- A股 -->
        <div 
          class="submenu-item"
          :class="{ active: $route.path.startsWith('/analysis/a-stock') }"
          @click="toggleAStockMenu"
        >
          A股
          <el-icon class="menu-icon" style="margin-left: auto;">
            <ArrowDown v-if="aStockMenuOpen" />
            <ArrowRight v-else />
          </el-icon>
        </div>
        
        <!-- A股三级菜单 -->
        <div v-show="aStockMenuOpen" class="submenu-level3">
          <div 
            class="submenu-item level3"
            :class="{ active: $route.path === '/analysis/a-stock/individual' }"
            @click="$router.push('/analysis/a-stock/individual')"
          >
            个股分析
          </div>
          <div 
            class="submenu-item level3"
            :class="{ active: $route.path === '/analysis/a-stock/portfolio' }"
            @click="$router.push('/analysis/a-stock/portfolio')"
          >
            投资组合
          </div>
          <div 
            class="submenu-item level3"
            :class="{ active: $route.path === '/analysis/a-stock/market' }"
            @click="$router.push('/analysis/a-stock/market')"
          >
            市场感知
          </div>
        </div>
        
        <!-- 港股 -->
        <div 
          class="submenu-item"
          :class="{ active: $route.path === '/analysis/hk-stock' }"
          @click="$router.push('/analysis/hk-stock')"
        >
          港股
        </div>
        
        <!-- 美股 -->
        <div 
          class="submenu-item"
          :class="{ active: $route.path === '/analysis/us-stock' }"
          @click="$router.push('/analysis/us-stock')"
        >
          美股
        </div>
      </div>
      
      <div 
        class="menu-item" 
        :class="{ active: $route.path === '/reports' }"
        @click="$router.push('/reports')"
      >
        <el-icon class="menu-icon"><Document /></el-icon>
        我的报告
      </div>
      
      <div 
        class="menu-item" 
        :class="{ active: $route.path === '/quantitative' }"
        @click="$router.push('/quantitative')"
      >
        <el-icon class="menu-icon"><DataAnalysis /></el-icon>
        量化分析
      </div>
    </div>
    
  </div>
</template>

<script>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

export default {
  name: 'Sidebar',
  setup() {
    const route = useRoute()
    const analysisMenuOpen = ref(true)
    const aStockMenuOpen = ref(false)
    
    const toggleAnalysisMenu = () => {
      analysisMenuOpen.value = !analysisMenuOpen.value
    }
    
    const toggleAStockMenu = () => {
      aStockMenuOpen.value = !aStockMenuOpen.value
    }
    
    // 监听路由变化，自动展开对应的菜单
    watch(() => route.path, (newPath) => {
      if (newPath.startsWith('/analysis/a-stock')) {
        aStockMenuOpen.value = true
        analysisMenuOpen.value = true
      } else if (newPath.startsWith('/analysis/hk-stock') || newPath.startsWith('/analysis/us-stock')) {
        analysisMenuOpen.value = true
      }
    }, { immediate: true })
    
    return {
      analysisMenuOpen,
      aStockMenuOpen,
      toggleAnalysisMenu,
      toggleAStockMenu
    }
  }
}
</script>
