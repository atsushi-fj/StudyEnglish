import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../main/HomeView.vue'
import LoginView from '@/users/LoginView.vue'

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
    {
      path: '/login',
      name: 'login',
      components: {
        default: LoginView,
      }
    },
  ],
})

export default router
