import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue' // Example: Import a Home component
import About from '../views/AboutView.vue' // Example: Import an About component
import Contact from '../views/ContactView.vue' // Example: Import a Contact component
import Login from '../views/LoginView.vue' // Example: Import a Login component
import Settings from '../views/SettingsView.vue' // Example: Import a Settings component
import Profile from '../views/ProfileView.vue' // Example: Import a Profile component
import Register from '../views/RegisterView.vue' // Example: Import a Register component
import NotFound from '../views/NotFoundView.vue' // Example: Import a NotFound component

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/contact', component: Contact },
  { path: '/login', component: Login },
  { path: '/settings', component: Settings },
  { path: '/profile', component: Profile },
  { path: '/register', component: Register },
  { path: '/:pathMatch(.*)*', component: NotFound },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
