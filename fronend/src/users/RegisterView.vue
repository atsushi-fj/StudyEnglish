<template>
  <div class="main">
    <div v-if="message" class="container">
      <div class="alert alert-danger mt-3" role="alert">{{ message }}</div>
    </div>
    <body class="text-center">
      <form @submit.prevent="register" action="" class="form-signin">
        <h1 class="h3 mb-3 font-weight-normal">会員登録</h1>
        <p class="no-wrap-text">サービスのご利用には会員登録が必要です。</p>
        <input v-model="email" type="email" placeholder="メールアドレス" class="form-control mt-5" id="inputEmail" required autofocus>
        <input v-model="username" type="text" placeholder="ユーザー名" class="form-control mt-3" id="inputUserName" required autofocus>
        <input v-model="password" type="password" placeholder="パスワード" class="form-control mt-3" id="inputPassword" required autofocus>
        <input v-model="passConfirm" type="password" placeholder="パスワード (確認)" class="form-control mt-3" id="inputPassconfirm" required autofocus>
        <button class="btn btn-lg btn-success btn-block mt-5" type="submit" @click="register">登録</button>
        <br>
        <br>
        <hr>
        <router-link style="text-decoration: none;" :to="{name: 'login'}">ログインはこちら</router-link>
      </form>
    </body>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      username: '',
      password: '',
      passConfirm: '',
      registerStatus: '',
      message: '',
    };
  },
  methods: {
    async register() {
      if (this.password !== this.passConfirm) {
          this.message = 'パスワードが一致しません'; 
          return;
      }
      try {
        const postData = {
          'email': String(this.email),
          'username': String(this.username),
          'password': String(this.password),
          'passConfirm': String(this.passConfirm),
        };

        const response = await axios.post('http://18.177.110.46/register', postData);
        this.registerStatus = response.data.status;
        if (this.registerStatus === 'SUCCESS') {
          this.$router.push({ name: 'login'} );
        } else if (this.registerStatus === 'USERNAME FAIL') {
          this.message = '入力されたユーザー名は既に使われています。'
        } else if (this.registerStatus === 'EMAIL FAIL') {
          this.message = '入力されたメールアドレスは既に登録されています。'
        } else if (this.registerStatus === 'FAIL') {
          this.message = '登録に失敗しました';

        }
      } catch(error) {
        console.log(error);
      } finally {
        this.email = '';
        this.username = '';
        this.password = '';
        this.passConfirm = '';
      }
    }
  }
  
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

.no-wrap-text {
  white-space: nowrap;
}

</style>