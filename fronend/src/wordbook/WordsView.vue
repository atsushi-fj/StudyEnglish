<template>
  <div class="main">
    <header id="page-header">
      <div class="container my-3 py-3">
        <div class="row">
          <div class="col-md-6 m-auto text-center">
            <h1>英単語一覧</h1>
            <p>合計: {{ this.numWords }}個</p>
          </div>
        </div>
      </div>
    </header>
    <section id="menu">
      <div class="container">
        <div class="row">
          <div v-if="authStore.userId === this.userId" class="col-md-1 d-flex justify-content-center mb-3">
            <router-link class="btn btn-secondary btn-menu" :to="`/${$route.params.wordbook_id}/create_word`">追加</router-link>
          </div>
          <div class="col-md-1 d-flex justify-content-center mb-3">
            <router-link class="btn btn-success btn-menu" :to="`/${$route.params.wordbook_id}/start_learning`">学習</router-link>
          </div>
        </div>
      </div>
    </section>
    <section id="list">
      <div class="container my-3">
        <table class="centered-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>英語</th>
              <th>日本語</th>
              <th v-if="authStore.userId === this.userId">削除</th>
            </tr>
          </thead>
          <tbody v-for="(word, index) in words" :key="index">
            <tr>
              <td>{{ calcWordId(index) }}</td>
              <td>{{ word.english }}</td>
              <td>{{ word.japanese }}</td>
              <td v-if="authStore.userId === this.userId"><a href="" class="btn btn-danger" @click.prevent="showModal(word.id)">削除</a></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
    <div class="container d-flex justify-content-center">
      <nav aria-label="Page navigation">
        <ul class="pagination">
          <li class="page-item" :class="{ disabled: currentPage === 1 }">
            <a class="page-link" href="#" @click.prevent="changePage(currentPage - 1)">Previous</a>
          </li>
          <li v-for="page in totalPages" :key="page" class="page-item" :class="{ active: currentPage === page }">
            <a class="page-link" href="#" @click.prevent="changePage(page)">{{ page }}</a>
          </li>
          <li class="page-item" :class="{ disabled: currentPage === totalPages }">
            <a class="page-link" href="#" @click.prevent="changePage(currentPage + 1)">Next</a>
          </li>
        </ul>
      </nav>
    </div>
    <div class="modal fade" id="delModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">削除確認</h1>
            <button type="button" class="btn-close" @click="hideModal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>この英単語帳を削除しますか?</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-danger" @click="deleteWord(deleteWordId)">削除する</button>
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
        words: [],
        userId: '0',
        numWords: 0,
        totalPages: 0,
        currentPage: 1,
        perPage: 7,
        deleteWordId: 1,
        deleteStatus: '',
    };
  },
  methods: {
    async deleteWord(id = 1) {
      const wordbookId = this.$route.params.wordbook_id;
      try {
        const response = await axios.delete(`http://18.177.110.46:8000/${wordbookId}/word`, {
          data: {
            word_id: id,
          }
        });
        this.deleteStatus = response.data.status;
        this.hideModal();
        this.fetchWords();
      } catch(error) {
        console.log(error)
      }
    },
    async fetchWords(page = 1) {
      try {
        const wordbookId = this.$route.params.wordbook_id;
        const response = await axios.get(`http://18.177.110.46:8000/${wordbookId}/words`, {
            params: {
              page: page,
              per_page: this.perPage,
            }
            });
            this.words = response.data.words;
            this.userId = response.data.user_id;
            this.numWords = response.data.num_words;
            this.totalPages = response.data.pages;
            this.currentPage = response.data.current_page;
          } catch(error) {
            console.log(error);
          }
        },
    changePage(page) {
        if (page >= 1 && page <= this.totalPages) {
            this.fetchWords(page);
        }
      },
      showModal(id) {
        this.deleteWordId = id
        const modal = new Modal(document.getElementById('delModal'));
        modal.show();
      },
      hideModal() {
        const modalElement = document.getElementById('delModal');
        const modal = Modal.getInstance(modalElement);
        modal.hide();
      },
      calcWordId(index) {
      return ((index + 1) + (this.perPage * (this.currentPage - 1)));
    }
    },
    mounted() {
      this.fetchWords();
    }
};
</script>
  
<style scoped>
.centered-table {
  width: 100%;
  border-collapse: collapse;
}

.centered-table th,
.centered-table td {
  text-align: center;
  vertical-align: middle;
  padding: 8px;
  border: 1px solid #ddd;
}

.btn-menu {
margin-top: auto;
width: 100%;
}
</style>
