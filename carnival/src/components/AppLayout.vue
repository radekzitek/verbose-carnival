<template>
    <div class="app-layout">
        <header class="app-header">
            <h1>My Awesome App</h1>
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
    background-color: #3030f0;
    /* Light gray background for header */
    color: white;
    /* White text for header */
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
    background-color: #3030f0;
    /* Slightly darker gray for sidebar */
    color: white;
    /* White text for sidebar */
    padding: 1rem;
}

.app-content {
    flex-grow: 1;
    /* Allow content to expand to fill remaining space */
    color: #3030f0;
    /* White text for content */
    padding: 1rem;
}

.app-footer {
    background-color: #3030f0;
    /* Dark background for footer */
    color: white;
    /* White text for footer */
    padding: 1rem;
    text-align: center;
    /* Center footer content */
}
</style>