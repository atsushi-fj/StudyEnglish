import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/main/HomeView.vue'
import LoginView from '@/users/LoginView.vue'
import RegisterView from '@/users/RegisterView.vue'
import WordBooks from '@/wordbook/WordBooks.vue'
import CreateBook from '@/wordbook/CreateBook.vue'
import AccountView from '@/users/AccountView.vue'
import Error403View from '@/error/Error403View.vue'
import Error404View from '@/error/Error404View.vue'
import UsersView from '@/users/UsersView.vue'
import WordsView from '@/wordbook/WordsView.vue'
import CreateWord from '@/wordbook/CreateWord.vue'
import LearnWord from '@/wordbook/LearnWord.vue'
import EndLearning from '@/wordbook/EndLearning.vue'

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
      path: '/users',
      name: 'users',
      components: {
        default: UsersView,
      }
    },
    {
      path: '/:user_id/account',
      name: 'account',
      components: {
        default: AccountView,
      },
      meta: { requiresAuth: true }
    },
    {
      path: '/:user_id/wordbooks',
      name: '/:user_id/wordbooks',
      components: {
        default: WordBooks,
      }
    },
    {
      path: '/:user_id/create_book',
      name: 'create_book',
      components: {
        default: CreateBook,
      },
      meta: { requiresAuth: true }
    },
    {
      path: '/:wordbook_id/words',
      name: 'words',
      components: {
        default: WordsView,
      }
    },
    {
      path: '/:wordbook_id/create_word',
      name: '/:wordbook_id/create_word',
      components: {
        default: CreateWord,
      }
    },
    {
      path: '/:wordbook_id/learn_word',
      name: '/:wordbook_id/learn_word',
      components: {
        default: LearnWord,
      }
    },
    {
      path: '/:wordbook_id/end_learning',
      name: '/:wordbook_id/end_learning',
      components: {
        default: EndLearning,
      }
    },
    {
      path: '/error403',
      name: 'error403',
      components: {
        default: Error403View,
      }
    },
    {
      path: '/:catchAll(.*)',
      name: 'error404',
      components: {
        default: Error404View,
      }
    },

  ],
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const isAuthenticated = localStorage.getItem('isAuthenticated') === 'true';
  const userId = localStorage.getItem('userId');
  const isAdmin = localStorage.getItem('isAdmin');
  const isUser = to.params.id === userId;
  
  if (isAdmin === '1') {
    next()
  } else if (requiresAuth && !isAuthenticated && !isUser) {
    next({ name: 'error403' })
  } else {
    next()
  }
})


export default router
