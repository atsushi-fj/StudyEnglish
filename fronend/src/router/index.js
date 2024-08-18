import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
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
import StartLearning from '@/wordbook/StartLearning.vue'
import PublicBooks from '@/wordbook/PublicBooks.vue'

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
      },
      meta: { requiresAdmin: true }
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
      },
      meta: { requiresAuth: true }
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
      },
      meta: { requiresAuth: true, requiresPublic: true}
    },
    {
      path: '/:wordbook_id/create_word',
      name: '/:wordbook_id/create_word',
      components: {
        default: CreateWord,
      },
      meta: { requiresAuth: true }
    },
    {
      path: '/:wordbook_id/learn_word',
      name: '/:wordbook_id/learn_word',
      components: {
        default: LearnWord,
      },
      meta: { requiresAuth: true, requiresPublic: true}
    },
    {
      path: '/:wordbook_id/start_learning',
      name: '/:wordbook_id/start_learning',
      components: {
        default: StartLearning,
      },
      meta: { requiresAuth: true, requiresPublic: true}
    },
    {
      path: '/:wordbook_id/end_learning',
      name: '/:wordbook_id/end_learning',
      components: {
        default: EndLearning,
      },
      meta: { requiresAuth: true, requiresPublic: true}
    },
    {
      path: '/public_books',
      name: 'public_books',
      components: {
        default: PublicBooks,
      },
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
  const authStore = useAuthStore();
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const requiresAdmin = to.matched.some(record => record.meta.requiresAdmin);
  const requiresPublic = to.matched.some(record => record.meta.requiresPublic);
  const isAuthenticated = authStore.isAuth === true;
  const isUser = to.params.id === authStore.userId;
  
  if (requiresAdmin && authStore.isAdmin === 0) {
    next({ name: 'error403'})
  } else if (requiresPublic) {
    next()
  } else if (requiresAuth && !isAuthenticated && !isUser) {
    next({ name: 'error403' })
  } else {
    next()
  }
})


export default router
