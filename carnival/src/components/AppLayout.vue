<template>
  <div class="app-layout">
    <header class="app-header">
      <p>Carnival</p>
    </header>

    <div class="app-main">
      <aside class="app-sidebar">
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/about">About</router-link></li>
          <li><router-link to="/contact">Contact</router-link></li>
        </ul>
      </aside>
      <main class="app-content">
        <RouterView></RouterView>
      </main>
    </div>

    <footer class="app-footer">
      <p>&copy; 2023 My Company</p>
    </footer>
  </div>
</template>

<script setup>
/* import { RouterLink, RouterView } from 'vue-router' */
</script>

<style scoped>
.app-layout {
  display: flex;
  flex-direction: column;
  /* Stack header, main, and footer vertically */
  min-height: 100vh;
  /* Ensure the layout takes up full viewport height */
}

.app-header {
  padding: 1rem;
  text-align: center;
  /* Center header content */
}

.app-main {
  display: flex;
  flex-grow: 1;
  /* Allow main section to expand to fill available space */
}

.app-sidebar {
  width: 300px;
  /* Fixed width for sidebar */
  padding: 1rem;
}

.app-content {
  flex-grow: 1;
  /* Allow content to expand to fill remaining space */
  padding: 1rem;
}

.app-footer {
  padding: 1rem;
  text-align: center;
  /* Center footer content */
}
</style>
