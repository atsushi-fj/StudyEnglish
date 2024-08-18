<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-white py-3">
    <div class="container px-5">
      <router-link class="navbar-brand" :to="{ name: 'home' }">
        <span class="fw-bolder text-success">Study English</span>
      </router-link>
      <button class="navbar-toggler collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 small fw-bolder">
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'home' }">ホーム</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'public_books' }">みんなの英単語帳</router-link>
          </li>
          <li v-if="authStore.isAuth" class="nav-item">
            <router-link class="nav-link" :to="{ path: `/${authStore.userId}/wordbooks` }">My英単語帳</router-link>
          </li>
          <li v-if="authStore.isAdmin === 1" class="nav-item">
            <router-link class="nav-link" :to="{ name: 'users' }">ユーザー</router-link>
          </li>
          <li v-if="authStore.username !== ''" class="nav-item">
            <router-link class="nav-link" :to="{ path: `/${authStore.userId}/account` }">{{ authStore.username }}</router-link>
          </li>
          <li v-if="authStore.isAuth" class="nav-item">
            <button class="nav-link" @click="logout">ログアウト</button>
          </li>
          <li v-else class="nav-item">
            <router-link class="nav-link" :to="{ name: 'login' }">ログイン</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>

</template>

<script>
import { useAuthStore } from '@/stores/auth';


export default {
  setup() {
    const authStore = useAuthStore();

    function logoutAuth() {
      authStore.logout();
    }

    return {authStore, logoutAuth}
  },
  methods: {
    logout() {
      this.logoutAuth();
      this.$router.push({ name: "login" });
    },
  },
};

</script>

<style>

</style>