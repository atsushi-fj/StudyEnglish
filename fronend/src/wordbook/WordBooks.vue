<template>
  <div class="main">
  <header id="page-header">
    <div class="container my-3 py-3">
      <div class="row">
        <div class="col-md-6 m-auto text-center">
          <h1>My英単語帳</h1>
        </div>
      </div>
    </div>
  </header>
  <div class="container my-2 py-2">
    <div class="row">
      <div class="col-md-2">
        <router-link class="btn btn-orange" :to="`/${$route.params.user_id}/create_book`">単語帳の作成</router-link>
      </div>
    </div>
  </div>
  <section id="list">
    <div class="container my-3">
      <div class="row">
        <div class="col-4 mb-4" v-for="wordbook in wordbooks" :key="wordbook.image">
          <div class="card h-100">
            <div class="card-body d-flex flex-column">
              <div class="mb-3 flex-grow-1 d-flex align-items-center justify-content-center">
                <img :src="`http://18.177.110.46/images/${wordbook.image}`" :alt="wordbook.image" class="img-fluid card-img-top">
              </div>
              <h3>
                <a href="" class="card-title text-decoration-none">
                  <span>{{ wordbook.title }}</span>
                </a>
              </h3>
              <p>{{ wordbook.date.slice(0, 10) }}</p>
              <div class="container">
                <div class="row">
                  <div class="col-md-3 d-flex justify-content-center">
                    <router-link class="btn btn-success btn-list" :to="`/${wordbook.id}/words`">一覧</router-link>
                  </div>
                  <div class="col-md-3 d-flex justify-content-center">
                    <a class="btn btn-danger btn-list" @click="showModal(wordbook.id)">削除</a>
                  </div>
                  <div class="col-md-5 d-flex justify-content-center">
                    <button v-if="wordbook.is_public === 'True'" class="btn btn-secondary btn-list" @click="togglePublic(wordbook.id)">公開しない</button>
                    <button v-else class="btn btn-secondary btn-list" @click="togglePublic(wordbook.id)">公開する</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
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
          <button type="button" class="btn btn-danger" @click="deleteBook(deleteBookId)">削除する</button>
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
        wordbooks: [],
        totalPages: 0,
        currentPage: 1,
        perPage: 3,
        deleteBookId: 1,
        deleteStatus: '',
    };
  },
  methods: {
    async deleteBook(id = 1) {
      const userId = this.$route.params.user_id;
      try {
        const response = await axios.delete(`http://18.177.110.46/${userId}/wordbooks`, {
          data: {
            book_id: id,
          }
        });
        this.deleteStatus = response.data.status;
        this.hideModal();
        this.fetchBooks();
      } catch(error) {
        console.log(error)
      }
    },
    async togglePublic(id = 1) {
      const userId = this.$route.params.user_id;
      try {
        axios.patch(`http://18.177.110.46/${userId}/wordbooks`, {
            book_id: id,
        });
        this.fetchBooks(this.currentPage);
      } catch(error) {
        console.log(error)
      }
    },
    async fetchBooks(page = 1) {
      const userId = this.$route.params.user_id;
      try {
          const response = await axios.get(`http://18.177.110.46/${userId}/wordbooks`, {
              params: {
                page: page,
                per_page: this.perPage,
              },
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            });
            console.log(response.data)
            this.wordbooks = response.data.wordbooks;
            this.totalPages = response.data.pages;
            this.currentPage = response.data.current_page;
          } catch(error) {
            console.log(error);
          }
        },
    changePage(page) {
        if (page >= 1 && page <= this.totalPages) {
            this.fetchBooks(page);
        }
      },
      showModal(id) {
        this.deleteBookId = id
        const modal = new Modal(document.getElementById('delModal'));
        modal.show();
      },
      hideModal() {
        const modalElement = document.getElementById('delModal');
        const modal = Modal.getInstance(modalElement);
        modal.hide();
      }
    },
    mounted() {
      this.fetchBooks();
    }
};
</script>

<style scoped>
.card {
  max-height: 30rem;
}

.card-img-top {
  max-height: 15rem;
  object-fit: cover;
  width: 100%;
}

.card-body {
  display: flex;
  flex-direction: column;
}

.btn-list {
  margin-top: auto;
  width: 100%;
}

.btn-orange {
  background-color: orange;
  color: white;
}

</style>
