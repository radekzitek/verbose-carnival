import './assets/main.css'

import { createApp } from 'vue'
import router from './router/index.js'; // Import the router

import App from './App.vue'

const app = createApp(App)
app.use(router) // Use the router

app.mount('#app')
