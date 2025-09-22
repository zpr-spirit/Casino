import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import IndividualStockAnalysis from '../views/IndividualStockAnalysis.vue'
import PortfolioAnalysis from '../views/PortfolioAnalysis.vue'
import MarketPerception from '../views/MarketPerception.vue'
import Reports from '../views/Reports.vue'
import Quantitative from '../views/Quantitative.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  // A股路由
  {
    path: '/analysis/a-stock/individual',
    name: 'AStockIndividual',
    component: IndividualStockAnalysis,
    meta: { market: 'A股', type: '个股分析' }
  },
  {
    path: '/analysis/a-stock/portfolio',
    name: 'AStockPortfolio',
    component: PortfolioAnalysis,
    meta: { market: 'A股', type: '投资组合' }
  },
  {
    path: '/analysis/a-stock/market',
    name: 'AStockMarket',
    component: MarketPerception,
    meta: { market: 'A股', type: '市场感知' }
  },
  // 港股路由
  {
    path: '/analysis/hk-stock',
    name: 'HkStock',
    component: () => import('../views/ComingSoon.vue'),
    meta: { market: '港股' }
  },
  // 美股路由
  {
    path: '/analysis/us-stock',
    name: 'UsStock',
    component: () => import('../views/ComingSoon.vue'),
    meta: { market: '美股' }
  },
  {
    path: '/reports',
    name: 'Reports',
    component: Reports
  },
  {
    path: '/quantitative',
    name: 'Quantitative',
    component: Quantitative
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
