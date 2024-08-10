<template>
  <div class="main">
    <div v-if="message" class="container">
      <div class="alert alert-danger mt-3" role="alert">
      {{ message }}
    </div>
    </div>
  <div id="body" class="text-center">
    <form @submit.prevent="login" action="" class="form-signin">
        <h1 class="h3 mb-3 font-weight-normal">ログインしてください</h1>
        <input v-model="email" type="email" placeholder="メールアドレス" class="form-control mt-5" id="inputEmail" required autofocus>
        <input v-model="password" type="password" placeholder="パスワード" class="form-control mt-3" id="inputPassword" required autofocus>
        <button class="btn btn-lg btn-success btn-block mt-5" type="submit" @click="login">ログイン</button>
    </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
        email: '',
        password: '',
        loginStatus: '',
        message: '',
    };
  },
  methods: {
    async login() {
      try {
        const postData = {
          'email': String(this.email),
          'password': String(this.password)    
        };

        const response = await axios.post('http://127.0.0.1:5000/login', postData);
        this.loginStatus = response.data.status;
        if (this.loginStatus === "SUCCESS") {
          localStorage.setItem('isAuthenticated', 'true');
          this.$router.push({ name: 'home' });
        } else if (this.loginStatus === "PASSWORD FAIL") {
          localStorage.setItem('isAuthenticated', 'false');
          this.message = "パスワードが一致しません";
        } else if (this.loginStatus === "USER FAIL") {
          localStorage.setItem('isAuthenticated', 'false');
          this.message = "入力されたユーザーは存在しません";
        }
    } catch(error) {
        console.log(error);
        this.loginStatus = "ERROR";
    } finally {
          this.email = '';
          this.password = '';
    }
        }
    }
  }
</script>

<style scoped>
#body {
  height: 100%;
}

#body {
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