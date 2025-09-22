<template>
  <div id="app">
    <div class="app-container">
      <!-- 左侧导航栏 -->
      <Sidebar />
      
      <!-- 主内容区域 -->
      <div class="main-content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'

export default {
  name: 'App',
  components: {
    Sidebar
  }
}
</script>
