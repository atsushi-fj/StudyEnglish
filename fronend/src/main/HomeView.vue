<template>
  <header class="py-5">
    <div class="container px-5 pb-5">
      <div class="row gx-5 align-items-center">
        <div class="col-xxl-5">
          <div class="text-center text-xxl-start">
            <h1 class="display-3 fw-bolder mb-5">
              <span class="text-gradient d-inline">自分だけの<br>英単語帳を<br>作ろう!</span>
            </h1>
            <div class="d-grid gap-3 d-sm-flex justify-content-sm-center justify-content xxl-start mb-3">
              <router-link v-if="authStore.isAuth" class="btn btn-success btn-lg px-5 py-3 me-sm-3 fs-6 fw-boder" :to="{ path: `/${authStore.userId}/wordbooks` }">はじめる</router-link>
              <router-link v-else class="btn btn-success btn-lg px-5 py-3 me-sm-3 fs-6 fw-boder" :to="{name: 'login'}">はじめる</router-link>
            </div>
          </div>
        </div>
        <div class="col-xxl-7">
          <div class="d-flex justify-content-center mt-5 mt-xxl-0">
            <div class="profile bg-gradient-primary-to-secondary">
              <img src="../assets/home.jpg" alt="..." height="600" width="600">
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import { useAuthStore } from '@/stores/auth';

export default {
  setup() {
    const authStore = useAuthStore();
    return {authStore};
  },
}
</script>

<style>

</style>
