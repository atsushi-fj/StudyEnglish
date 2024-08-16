<template>
  <div class="main">
  <div class="container mt-5">
    <div class="row">
      <div class="col-md-10 offset-md-1">
        <form @submit.prevent="checkAnswer(answer, word.japanese)" class="shadow p-4" v-for="(word, index) in words" :key="index">
          <div class="d-flex justify-content-center">
            <p class="word-size"><strong>{{ word.english }}</strong></p>
          </div>
          <div class="mt-3 d-flex justify-content-center">
            <input v-model="answer" type="text" class="input-size" placeholder="答えを記入">
          </div>
          <div class="mt-5 d-flex justify-content-center">
            <button type="submit" class="btn btn-success btn-lg">解答する</button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <transition name="fade" @after-enter="animationEnd(currentPage + 1)">
    <div v-if="showMessage" :class="animationClass" class="message-container">
        <div v-if="answer === correctAnswer" class="message correct">
          <span class="icon correct-icon"></span>
          <p class="mt-3"><strong>正解！</strong></p>
        </div>
        <div v-else class="message incorrect">
          <span class="icon incorrect-icon"></span>
          <p class="mt-5"><strong>不正解！</strong></p>
        </div>
      </div>
  </transition>
  </div>
</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
          words: [],
          totalPages: 0,
          currentPage: 1,
          perPage: 1,
          deleteWordId: 1,
          deleteStatus: '',
          answer: '',
          correctAnswer: '',
          showMessage: false,
          animationClass: '',
          endLeanring: false,
          numCorrect: 0,
      };
    },
    methods: {
      async fetchWords(page = 1) {
        try {
            this.showMessage = false;
            const wordbookId = this.$route.params.wordbook_id;
            const response = await axios.get(`http://127.0.0.1:5000/${wordbookId}/words`, {
                params: {
                  page: page,
                  per_page: this.perPage,
                }
              });
              this.answer = '';
              this.words = response.data.words;
              this.totalPages = response.data.pages;
              this.currentPage = response.data.current_page;
            } catch(error) {
              console.log(error);
            }
          },
      changePage(page) {
          if (page >= 1 && page <= this.totalPages) {
              this.fetchWords(page);
          } else if (page > this.totalPages) {
            const wordbookId = this.$route.params.wordbook_id;
            this.$router.push({path: `/${wordbookId}/end_learning`, query: {numWords: this.totalPages, numCorrect: this.numCorrect}});
          }
        },
      checkAnswer(ans, correctAns) {
        this.correctAnswer = correctAns;
        if (ans === correctAns) {
            this.animationClass = 'correct';
            this.numCorrect += 1;
        } else {
            this.animationClass = 'incorrect';
        }

        this.showMessage = true;

        setTimeout(() => {
            this.showMessage = false;
        }, 2000);
      },
      animationEnd(page) {
        this.showMessage = false;
        this.changePage(page);
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

.btn-danger {
margin-top: auto;
width: 100%;
}

.btn-secondary {
margin-top: auto;
width: 100%;
}

.word-size {
  font-size: 10vw;
  overflow-wrap: break-word;
}

.input-size {
  width: 700px;
  height: 80px;
  font-size: 60px;
}

.correct {
  animation: correct-animation 1s ease-out;
}

.incorrect {
  animation: incorrect-animation 1s ease-out;
}

.icon {
  width: 300px;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 60px;
}

.correct-icon {
  border-radius: 50%; /* 円形にする */
  border: 30px solid; /* 円の枠線の太さ */
  box-sizing: border-box; /* ボーダーをサイズに含める */
  border-color: red;
}

.incorrect-icon::before,
.incorrect-icon::after {
  content: '';
  position: absolute;
  width: 300px;
  height: 50px;
  background-color: blue;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(45deg);
}

.incorrect-icon::after {
  transform: translate(-50%, -50%) rotate(-45deg);
}

.message-container {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  color: black;
  font-size: 50px;
  text-align: center;
}

.message {
  font-size: 50px;
  padding: 20px;
  border-radius: 8px;
}

</style>
