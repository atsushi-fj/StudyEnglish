import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../main/HomeView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        default: HomeView,
      }
    },
  ],
})

export default router
