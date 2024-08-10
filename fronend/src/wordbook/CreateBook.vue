<template>
    <div class="container mt-5">
    <div class="row">
        <div class="col-md-6 offset-md-3">
            <div class="mb-3">
                <h3>英単語帳の作成</h3>
            </div>
            <form accept="" class="shadow p-4">                  
                <div class="mb-3">
                    <label for="title">タイトル</label>
                    <input v-model="title" type="text" class="form-control" name="title" id="title" placeholder="タイトル">
                </div>
                <div class="mb-3">
                    <label for="image">画像のアップロード</label>
                    <br>
                    <input type="file" id="image">
                </div>
                <div class="mb-3">
                    <button type="submit" class="btn btn-success" @click="createBook">作成</button>
                </div>
            </form>
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
            message: ''
        };
    },
    methods: {
        handleFileChange(event) {
            const file = event.target.files[0]
            if (file) {
                this.picture = file;
            }
        },
        async createBook() {
            try {
                const response = await axios.post(`http://127.0.0.1:5000/${this.$route.params.user_id}/create_book`,
                {
                    title: this.title,
                    picture: this.picture
                });
                this.message = response.data.message;
                if (response.status === 200) {
                    this.$router.push({ name: 'home'}
                    )
                }
            } catch (error) {
                this.message = error.response.data.message;
            }
        }

        }

    }

</script>

<style>
</style>