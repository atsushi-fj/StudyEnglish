import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/main/HomeView.vue'
import LoginView from '@/users/LoginView.vue'
import RegisterView from '@/users/RegisterView.vue'
import WordBooks from '@/wordbook/WordBooks.vue'
import CreateBook from '@/wordbook/CreateBook.vue'
import Error403View from '@/error/Error403View.vue'

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
    {
      path: '/register',
      name: 'register',
      components: {
        default: RegisterView,
      }
    },
    {
      path: '/:user_id',
      name: 'my_wordbooks',
      components: {
        default: WordBooks,
      }
    },
    {
      path: '/:user_id/create_book',
      name: 'create_book',
      components: {
        default: CreateBook,
      }
    },
    {
      path: '/:user_id/create_book',
      name: 'create_book',
      components: {
        default: CreateBook,
      }
    },
    {
      path: '/error403',
      name: 'error403',
      components: {
        default: Error403View,
      }
    },

  ],
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  const isAuthenticated = localStorage.getItem('isAuthenticated') === 'true'

  if (requiresAuth && !isAuthenticated) {
    next({ name: 'error403' })
  } else {
    next()
  }
})


export default router
