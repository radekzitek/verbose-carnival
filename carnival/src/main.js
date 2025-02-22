import './assets/main.css'
import 'primeicons/primeicons.css'

import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'
import 'mdb-vue-ui-kit/css/mdb.min.css'
import router from './router/index.js' // Import the router

import App from './App.vue'

const app = createApp(App)
app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
}) // Use PrimeVue

app.use(router) // Use the router

app.mount('#app')
