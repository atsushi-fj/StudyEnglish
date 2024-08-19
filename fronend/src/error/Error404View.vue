<template>
  <div class="main">
    <div class="container my-3 py-3">
      <div class="row">
        <div class="col-md-3">
          <router-link class="btn btn-success w-90" :to="{ name: 'home' }">メインページへ戻る</router-link>
        </div>
      </div>
    </div>
    <header id="page-header">
      <div class="container my-3 py-3">
        <h1>ページが見つかりません</h1>
        <p>誠に恐れ入りますが、お客様がアクセスしたページにが見つかりませんでした。
        <br>
        既に削除されたか、アドレスが間違っている可能性がございます。</p>
      </div>
    </header>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
