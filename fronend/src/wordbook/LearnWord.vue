<template>
  <div class="main">
    <div class="progress-bar">
      <div class="progress" :style="{ width: progressWidth + '%' }"></div>
    </div>
  <div class="container mt-5">
    <div class="row">
      <div class="col-md-10 offset-md-1">
        <form @submit.prevent="checkAnswer(answer, word.japanese)" class="shadow p-4" v-for="(word, index) in words" :key="index">
          <div class="d-flex justify-content-center">
            <p class="word-size"><strong>{{ word.english }}</strong></p>
            <button type="button" class="btn btn-secondary btn-sm  mx-3 px-3 my-5 btn-audio" @click="playAudio(word.english)">音声再生</button>
            <audio ref="audio"></audio>
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
  <div class="container mt-5">
    <div class="row">
      <div class="col-md-3 offset-md-1">
        <button class="btn btn-orange btn-lg" @click="toggleTerminal">終了する</button>
      </div>
    </div>
  </div>
    <transition name="fade" @after-enter="animationEnd(currentPage + 1)">
      <div v-if="showMessage" :class="animationClass" class="message-container">
        <div v-if="answer === correctAnswer" class="message correct">
          <span class="icon correct-icon"></span>
          <p class="pt-5 mt-5 ans-size"><strong>正解！</strong></p>
        </div>
        <div v-else class="message incorrect">
          <span class="icon incorrect-icon"></span>
          <p class="pt-5 mt-5 ans-size"><strong>不正解！</strong></p>
          <p class="mt-3 ans-size">正しい答え: {{ correctAnswer }}</p>
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
      answer: '',
      correctAnswer: '',
      showMessage: false,
      animationClass: '',
      numCorrect: 0,
      };
    },
    computed: {
      progressWidth() {
        return (this.currentPage / this.totalPages) * 100;
      }
    },
    methods: {
      async playAudio(text) {
        try {
          const response = await axios.post(`http://18.177.110.46/speak`, {
            text: text
          }, { responseType: 'blob' });
          const audioBlob = new Blob([response.data], { type: 'audio/mp3'});  
          const audioUrl = URL.createObjectURL(audioBlob);
          const audioElement = new Audio(audioUrl);
          await audioElement.play()
        } catch (error) {
          console.log(error);
        }
      },
      async fetchWords(page = 1) {
        try {
            this.showMessage = false;
            const wordbookId = this.$route.params.wordbook_id;
            const response = await axios.get(`http://18.177.110.46/${wordbookId}/words`, {
                params: {
                  page: page,
                  per_page: this.perPage,
                  sort_option: this.$route.query.sortOption, 
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
      },
      toggleTerminal() {
        const wordbookId = this.$route.params.wordbook_id;
        this.$router.push({path: `/${wordbookId}/end_learning`, query: {numWords: this.currentPage-1, numCorrect: this.numCorrect}});
      },
      },
      mounted() {
        this.fetchWords();
      }
  };
</script>
  
<style scoped>

.word-size {
  font-size: 5vw;
  overflow-wrap: break-word;
}

.ans-size {
  font-size: 3vw;
  overflow-wrap: break-word;
}

.input-size {
  width: 30vw;
  height: 4vw;
  font-size: 3vw;
}

.correct {
  animation: correct-animation 1s ease-out;
}

.incorrect {
  animation: incorrect-animation 1s ease-out;
}

.icon {
  width: 15vw;
  height: 15vw;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20vw;
}

.correct-icon {
  border-radius: 50%; /* 円形にする */
  border: 1vw solid; /* 円の枠線の太さ */
  box-sizing: border-box; /* ボーダーをサイズに含める */
  border-color: red;
}

.incorrect-icon::before,
.incorrect-icon::after {
  content: '';
  position: absolute;
  width: 15vw;
  height: 2vw;
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
  font-size: 10vw;
  text-align: center;
}

.message {
  font-size: 10vw;
  padding: 5vw;
  border-radius: 2vw;
}

.btn-orange {
  background-color: orange;
  color: white;
}

.btn-audio {
  width: 90px;
  height: 40px;
}

.progress-bar {
  width: 100%;
  background-color: #f3f3f3;
}
.progress {
  height: 20px;
  background-color: #4caf50;
}
</style>
