import './assets/main.css'
import 'mdb-vue-ui-kit/css/mdb.min.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router/index.js' // Import the router
// import { useAuthStore } from './stores/authStore.js' // Import the store
import App from './App.vue'

const pinia = createPinia()

const app = createApp(App)

app.use(pinia) // Use the pinia store
app.use(router) // Use the router

// const authStore = useAuthStore(pinia) // Create the store instance AFTER pinia is installed
// authStore.setIsAuthenticated(false) // Set the initial state - REMOVE THIS LINE

app.mount('#app')
