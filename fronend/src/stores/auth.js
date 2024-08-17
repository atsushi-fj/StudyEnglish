import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuth: false,
    userId: 0,
    isAdmin: 0,
  }),
  actions: {
    login() {
      this.isAuth = true;
    },
    logout() {
      this.isAuth = false;
      this.userId = 0;
      this.isAdmin = 0;
    }
  }
})