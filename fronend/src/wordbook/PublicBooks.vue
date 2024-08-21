<template>
    <div class="main">
    <header id="page-header">
      <div class="container my-3 py-3">
        <div class="row">
          <div class="col-md-6 m-auto text-center">
            <h1>みんなの英単語帳</h1>
          </div>
        </div>
      </div>
    </header>
    <div class="container position-relative">
      <div class="row justify-content-center">
        <div class="col-xl-6">
          <div class="text-center">
            <form @submit.prevent="fetchBooks()" class="form-subscribe">
              <div class="row">
                <div class="col">
                  <input v-model="tempSearchQuery" class="form-control form-control-lg" type="text" placeholder="タイトル">
                </div>
                <div class="col-auto"><button class="btn btn-success btn-lg" id="submitButton" type="submit">検索する</button></div>
              </div>
            </form>
          </div>
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
                <p>作成日: {{ wordbook.date.slice(0, 10) }}</p>
                <p>ユーザー名: {{ wordbook.author.slice(9,) }}</p>
                <div class="container">
                  <div class="row">
                    <div class="col-md-3 d-flex justify-content-center">
                      <router-link class="btn btn-success btn-list" :to="`/${wordbook.id}/words`">一覧</router-link>
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
  </div>
</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
          wordbooks: [],
          totalPages: 0,
          currentPage: 1,
          perPage: 3,
          searchQuery: '',
          tempSearchQuery: '',
      };
    },
    methods: {
      async fetchBooks(page = 1) {
        try {
            this.searchQuery = this.tempSearchQuery;
            const response = await axios.get('http://18.177.110.46/public_wordbooks', {
                params: {
                  q: this.searchQuery,
                  page: page,
                  per_page: this.perPage,
                },
                headers: {
                  'Content-Type': 'multipart/form-data'
                }
              });
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

.choices__list {
  margin: 0;
  padding-left: 0;
  list-style: none
}
  
.choices__list--multiple {
  display: inline
}

.s004 form .inner-form .input-field .choices .choices__inner {
  min-height: 70px;
  width: 100%;
  background: 0 0;
  border: 0;
  background: #fff;
  display: block;
  width: 100%;
  padding: 10px 70px 10px 32px;
  font-size: 18px;
  color: #666;
  border-radius: 34px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  -ms-flex-align: center;
  align-items: center
}
</style>
