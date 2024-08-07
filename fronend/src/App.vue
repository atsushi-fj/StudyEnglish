<template>
  <NavbarView />
  <router-view />
</template>

<script>
import NavbarView from './components/NavbarView.vue'

export default {
  name: 'App',
  components: {
    NavbarView
  }
}
</script>

<style>

</style>
