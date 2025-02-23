import './assets/styles/main.scss'
import 'mdb-vue-ui-kit/css/mdb.min.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router/index.js' // Import the router
import App from './App.vue'

const pinia = createPinia()

const app = createApp(App)

app.use(pinia) // Use the pinia store
app.use(router) // Use the router

app.mount('#app')
