<template>
  <NavbarView />
  <div class="wrapper">
    <router-view />
    <FooterView />
  </div>
</template>

<script>
import NavbarView from './components/NavbarView.vue'
import FooterView from './components/FooterView.vue';

export default {
  name: 'App',
  components: {
    NavbarView,
    FooterView
  }
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
}

.wrapper {
  display: grid;
  grid-template-rows: 1fr auto;
  min-height: 100vh;
}
</style>
