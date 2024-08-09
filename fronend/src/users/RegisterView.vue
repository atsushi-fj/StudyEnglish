<template>
  <body class="text-center">
    <form action="" class="form-signin">
      <h1 class="h3 mb-3 font-weight-normal">会員登録してください</h1>
      <input v-model="email" type="email" placeholder="メールアドレス" class="form-control mt-5" id="inputEmail" required autofocus>
      <input v-model="password" type="password" placeholder="パスワードを追加 (半角英数字)" class="form-control mt-3" id="inputPassword" required autofocus>
      <button class="btn btn-lg btn-success btn-block mt-5" type="submit">登録</button>
    </form>
  </body>
</template>
  
<script>
  
  export default {
  
  }
  </script>
  
  <style scoped>
  body {
    height: 100%;
  }
  
  body {
    display: -ms-flexbox;
    display: -webkit-box;
    display: flex;
    -ms-flex-align: center;
    -ms-flex-pack: center;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    padding-top: 40px;
    padding-bottom: 40px;
  }
  
  .form-signin {
    width: 100%;
    max-width: 330px;
    padding: 15px;
    margin: 0 auto;
  }
  
  .form-signin .form-control {
    position: relative;
    box-sizing: border-box;
    height: auto;
    padding: 10px;
    font-size: 16px;
  }
  
  .form-signin .form-control:focus {
    z-index: 2;
  }
  
  </style>