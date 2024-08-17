<template>
  <div class="main">
  <div class="container my-3 py-3 d-flex justify-content-center">
      <h1>{{ $route.query.numWords }}問中{{ $route.query.numCorrect }}問正解でした。</h1>
  </div>
  <div class="container mt-5">
    <div class="row">
      <div class="col-md-2 offset-md-4 mb-3">
        <router-link class="btn btn-success" :to="`/${$route.params.wordbook_id}/start_learning`">もう一度<br>挑戦する</router-link> 
      </div>
      <div class="col-md-2 mb-3">
        <router-link class="btn btn-secondary" :to="`/${$route.params.wordbook_id}/words`">英単語帳一覧<br>に戻る</router-link> 
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {

}
</script>

<style scoped>
.btn {
  width: 80%;
  height: 100%;
}

</style>