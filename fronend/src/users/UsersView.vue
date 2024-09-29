<template>
  <div class="main">
    <header id="page-header">
      <div class="container my-3 py-3">
        <div class="row">
          <div class="col-md-6 m-auto text-center">
            <h1>ユーザー管理</h1>
          </div>
        </div>
      </div>
    </header>
    <section id="list">
      <div class="container my-3">
        <table class="centered-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>ユーザー名</th>
              <th>メールアドレス</th>
              <th>管理者</th>
              <th>変更</th>
            </tr>
          </thead>
          <tbody v-for="user in users" :key="user.id">
            <tr>
              <td>{{ user.id }}</td>
              <td>{{ user.username }}</td>
              <td>{{ user.email }}</td>
              <td>{{ user.administrator }}</td>
              <td><router-link class="btn btn-success" :to="`/${user.id}/account`">変更</router-link></td>
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
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
        users: [],
        totalPages: 0,
        currentPage: 1,
        perPage: 8,
    };
  },
  methods: {
    async fetchUsers(page = 1) {
      try {
          const response = await axios.get('http://18.177.110.46:8000/users', {
              params: {
                page: page,
                per_page: this.perPage,
              }
            });
            this.users = response.data.users;
            this.totalPages = response.data.pages;
            this.currentPage = response.data.current_page;
          } catch(error) {
            console.log(error);
          }
        },
    changePage(page) {
        if (page >= 1 && page <= this.totalPages) {
            this.fetchUsers(page);
        }
      }
    },
    mounted() {
      this.fetchUsers();
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
</style>
