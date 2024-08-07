<template>
  <div>
  <h2>Login</h2>
  <form @submit.prevent="login">
      <input v-model="username" type="text" placeholder="Username">
      <input v-model="password" type="password" placeholder="Password">
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>

export default {

}
</script>

<style>

</style>