import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/main/HomeView.vue'
import LoginView from '@/users/LoginView.vue'
import RegisterView from '@/users/RegisterView.vue'
import WordBooks from '@/wordbook/WordBooks.vue'
import CreateBook from '@/wordbook/CreateBook.vue'

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
      path: '/:id',
      name: 'my_wordbooks',
      components: {
        default: WordBooks,
      }
    },
    {
      path: '/:id/create_book',
      name: 'create_book',
      components: {
        default: CreateBook,
      }
    }
  ],
})

export default router
