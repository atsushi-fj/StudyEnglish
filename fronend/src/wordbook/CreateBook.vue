<template>
  <div class="main">
    <div v-if="message" class="container">
      <div class="alert alert-warning mt-3" role="alert">{{ message }}</div>
    </div>
    <div class="container mt-5">
    <div class="row">
        <div class="col-md-6 offset-md-3">
            <div class="mb-3">
                <h3>英単語帳の作成</h3>
            </div>
            <form class="shadow p-4">
                <div class="mb-3">
                    <label for="title">タイトル</label>
                    <input v-model="title" type="text" class="form-control" name="title" id="title" placeholder="タイトル">
                </div>
                <div class="mb-3">
                    <label for="image">画像のアップロード</label>
                    <br>
                    <input type="file" id="image" @change="onFileChange">
                </div>
                <div class="mb-3">
                    <button type="submit" class="btn btn-success" @click="createBook">作成</button>
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
    title: '',
    picture: null,
    message: '',
    createStatus: '',
    };
  },
  methods: {
    onFileChange(event) {
      this.picture = event.target.files[0];
    },
    async createBook() {
      const formData = new FormData();
      formData.append('title', this.title);
      formData.append('picture', this.picture);
      console.log(formData);
      try {
        const response = await axios.put(`http://127.0.0.1:5000/${this.$route.params.user_id}/create_book`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
      });
        if (response.data.status === 'Create successful') {
            this.message = '新しい英単語帳を作成しました。';
        } else if (response.data.status === 'FAIL') {
            this.message = '英単語帳を作成することができませんでした。';
        }
        } catch (error) {
            console.log("error")
        }
    }

        }

    }

</script>

<style>
</style>