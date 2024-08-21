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
import axios from 'axios'

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
      name: 'wordbooks',
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
      name: 'create_word',
      components: {
        default: CreateWord,
      },
      meta: { requiresAuth: true }
    },
    {
      path: '/:wordbook_id/learn_word',
      name: 'learn_word',
      components: {
        default: LearnWord,
      },
      meta: { requiresAuth: true, requiresPublic: true}
    },
    {
      path: '/:wordbook_id/start_learning',
      name: 'start_learning',
      components: {
        default: StartLearning,
      },
      meta: { requiresAuth: true, requiresPublic: true}
    },
    {
      path: '/:wordbook_id/end_learning',
      name: 'end_learning',
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

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore();
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const requiresAdmin = to.matched.some(record => record.meta.requiresAdmin);
  const requiresPublic = to.matched.some(record => record.meta.requiresPublic);
  const isAuthenticated = authStore.isAuth === true;
  const isUser = to.params.id === authStore.userId;
  let isPublicBook = false

  if (to.name === 'words' || to.name === 'start_learning' || to.name === 'learn_word' || to.name === 'end_learning') {
    try {
      const respose = await axios.get(`http://18.177.110.46/${to.params.wordbook_id}/get_wordbook_id`);
      isPublicBook = respose.data.is_public;
    } catch(error) {
      console.log(error)
    }
  }
  if (requiresAdmin && authStore.isAdmin === 0) {
    next({ name: 'error403'});
  } else if (requiresPublic && isPublicBook) {
    next()
  } else if (requiresAuth && !isAuthenticated && !isUser) {
    next({ name: 'error403' });
  } else {
    next();
  }
})

export default router
