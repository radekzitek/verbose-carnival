import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/HomeView.vue'; // Example: Import a Home component
import About from '../views/AboutView.vue'; // Example: Import an About component
import Contact from '../views/ContactView.vue'; // Example: Import a Contact component

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/contact', component: Contact },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;