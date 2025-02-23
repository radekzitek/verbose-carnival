<template>
  <div v-for="(item, index) in sidebarItems" :key="index">
    <a :href="item.url" target="_blank" class="sidebar-item">
      <div class="text-lg font-bold">
        {{ item.oline }}
        <br />
      </div>
      <div class="text-sm text-stone-400">
        {{ item.uline }}
      </div>
    </a>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const sidebarItems = ref([
  {
    oline: 'MDB for Vue',
    uline: 'Material Design for Bootstrap',
    url: 'https://mdbootstrap.com/docs/vue/',
  },
  {
    oline: 'Tailwind CSS',
    uline: 'A utility-first CSS framework',
    url: 'https://tailwindcss.com/docs',
  },
  {
    oline: 'PrimeVue',
    uline: 'Next-generation UI Component suite for Vue',
    url: 'https://primevue.org/introduction/',
  },
])
</script>

<style scoped>
.sidebar-item {
  display: block;
  margin-bottom: 1rem;
  text-decoration: none;
  color: inherit;
}
</style>
