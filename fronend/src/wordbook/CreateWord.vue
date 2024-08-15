<template>
    <div class="main">
      <div v-if="message" class="container">
        <div class="alert alert-warning mt-3" role="alert">{{ message }}</div>
      </div>
      <div class="container mt-5">
      <div class="row">
          <div class="col-md-6 offset-md-3">
              <div class="mb-3">
                  <h3>英単語の作成</h3>
              </div>
              <form @submit.prevent="createWord" class="shadow p-4">
                  <div class="mb-3">
                      <label for="english">英語</label>
                      <input v-model="english" type="text" class="form-control" name="english" id="english" placeholder="英語">
                  </div>
                  <div class="mb-3">
                      <label for="japanese">日本語</label>
                      <input v-model="japanese" type="text" class="form-control" name="japanese" id="japanese" placeholder="日本語">
                  </div>
                  <div class="mb-3">
                      <button type="submit" class="btn btn-success">作成</button>
                  </div>
              </form>
          </div>
      </div>
    </div>
  </div>  
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
      japanese: '',
      english: '',
      message: '',
      createStatus: '',
      };
    },
    methods: {
      async createWord() {
        const putData = {
            'japanese': this.japanese,
            'english': this.english,
        }
        try {
          const response = await axios.put(`http://127.0.0.1:5000/${this.$route.params.wordbook_id}/word`, putData);
          console.log(response.data)
          if (response.data.status === 'Create successful') {
              this.message = '新しい英単語を作成しました。';
          } else if (response.data.status === 'FAIL') {
              this.message = '英単語を作成することができませんでした。';
          }
          } catch (error) {
              console.log(error)
          }
      }
  
          }
  
      }
  
  </script>
  
  <style>
  </style>