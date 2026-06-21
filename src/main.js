import { createApp } from 'vue'
import './assets/style.css'
import App from './App.vue'
import router from './router'

if ('scrollRestoration' in history) {
  history.scrollRestoration = 'manual'
}

const app = createApp(App)
app.use(router)
app.mount('#app')
