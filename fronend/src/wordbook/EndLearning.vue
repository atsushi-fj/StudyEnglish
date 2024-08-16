<template>
  <div class="main">
  <p>{{ $route.query.numWords }}</p>
  <p>{{ $route.query.numCorrect }}</p>
  <div class="container my-3 py-3 d-flex justify-content-center">
      <h1>{{ $route.query.numWords }}問中{{ $route.query.numCorrect }}問正解でした。</h1>
      <p>誠に恐れ入りますが、お客様がアクセスしたページにはアクセスできませんでした。
      <br>
      指定されたページへのアクセスが許可されておりません。</p>
  </div>
  
</div>
</template>

<script>
export default {

}
</script>

<style>

</style>