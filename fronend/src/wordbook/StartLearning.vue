<template>
  <div class="main">
  <div class="container my-3 py-3 d-flex justify-content-center">
      <h1>英単語学習を始める</h1>
  </div>
  <div class="container mt-5">
    <div class="row mb-5 text-center">
      <div class="col-md-2 offset-md-5">
        <select class="form-select-lg" aria-label="Default select example" v-model="selectedOption">
          <option value="" disabled>単語の順番を選ぶ</option>
          <option value="random">ランダム</option>
          <option value="asc">古い順</option>
          <option value="desc">新しい順</option>
        </select>
      </div>
    </div>
    <div class="row mb-3 text-center">
      <div class="col-md-2 offset-md-5">
        <router-link :class="{ disabled: !selectedOption }" class="btn btn-success btn-lg" :to="{ path: `/${$route.params.wordbook_id}/learn_word`, query: {sortOption: selectedOption}}">開始する</router-link>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedOption: '',
    }
  }

}
</script>

<style scoped>
.btn {
  width: 80%;
}

</style>