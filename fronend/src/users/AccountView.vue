<template>
  <div class="main">
    <div v-if="message" class="container">
      <div class="alert alert-danger mt-3" role="alert">{{ message }}</div>
    </div>
    <body class="text-center">
      <form @submit.prevent="update" action="" class="form-signin">
        <h1 class="h3 mb-3 font-weight-normal">ユーザー更新</h1>
        <p>ユーザー情報を更新してください。</p>
        <input v-model="email" type="email" placeholder="メールアドレス" class="form-control mt-5" id="inputEmail" required autofocus>
        <input v-model="username" type="text" placeholder="ユーザー名" class="form-control mt-3" id="inputUserName" required autofocus>
        <input v-model="password" type="password" placeholder="新パスワード" class="form-control mt-3" id="inputPassword" required autofocus>
        <input v-model="passConfirm" type="password" placeholder="新パスワード (確認)" class="form-control mt-3" id="inputPassconfirm" required autofocus>
        <button class="btn btn-lg btn-success btn-block mt-5 mx-3" type="submit" @click="update">更新</button>
        <button :disabled="authStore.isAdmin !== 1" class="btn btn-lg btn-danger btn-block mt-5 mx-3" type="button" @click="showModal">削除</button>
      </form>
    </body>
    <!-- Modal -->
    <div class="modal fade" id="delModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">削除確認</h1>
            <button type="button" class="btn-close" @click="hideModal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>このユーザーを削除しますか?</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-danger" @click="deleteUser">削除する</button>
            <button type="button" class="btn btn-secondary" @click="hideModal">キャンセル</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import { Modal } from 'bootstrap';
  import { useAuthStore } from '@/stores/auth';
  
  export default {
    setup() {
      const authStore = useAuthStore();
      return {authStore}
    },
    data() {
      return {
        email: '',
        username: '',
        password: '',
        passConfirm: '',
        updateStatus: '',
        deleteStatus: '',
        message: '',
      };
    },
    mounted() {
        this.fetchUserData();
    },
    methods: {
      async fetchUserData() {
        const userId = this.$route.params.user_id;
        try {
            const response = await axios.get(`http://18.177.110.46:8000/${userId}/account`);
            this.email = response.data.email;
            this.username = response.data.username;
        } catch(error) {
            console.log(error)
        }
      },
      async update() {
        if (this.password !== this.passConfirm) {
            this.message = 'パスワードが一致しません'; 
            return;
        }
        try {
          const userId = this.$route.params.user_id;
          const putData = {
            'email': String(this.email),
            'username': String(this.username),
            'password': String(this.password),
          };
  
          const response = await axios.put(`http://18.177.110.46:8000/${userId}/account`, putData);
          this.updateStatus = response.data.status;
          if (this.updateStatus === 'SUCCESS') {
            this.$router.push({ name: 'home'} );
          } else if (this.registerStatus === 'USERNAME FAIL') {
            this.message = '入力されたユーザー名は既に使われています。'
          } else if (this.updateStatus === 'EMAIL FAIL') {
            this.message = '入力されたメールアドレスは既に登録されています。'
          } else if (this.updateStatus === 'FAIL') {
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
      },
      async deleteUser() {
        try {
            const userId = this.$route.params.user_id;
            const response = await axios.delete(`http://18.177.110.46:8000/${userId}/account`);
            this.deleteStatus = response.data.status;
            this.hideModal();
            if (this.deleteStatus === 'SUCCESS') {
                this.$router.push({ name: 'home'} );
            }
        } catch(error) {
            console.log(error)
        }
      },
      showModal() {
        const modal = new Modal(document.getElementById('delModal'));
        modal.show();
      },
      hideModal() {
        const modalElement = document.getElementById('delModal');
        const modal = Modal.getInstance(modalElement);
        modal.hide();
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
  </style>
  