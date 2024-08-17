import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import router from './router/index'
import { createPinia } from 'pinia'


if (!localStorage.getItem('isAuthenticated')) {
    localStorage.setItem('isAuthenticated', 'false');
}

const app = createApp(App)
const pinia = createPinia()
app.use(pinia)
app.use(router)
app.mount('#app')