<template>
  <div id="app">
    <AppLayout />
  </div>
</template>

<script>
import AppLayout from './components/AppLayout.vue' // Import the layout component

export default {
  components: {
    AppLayout, // Register the component
  },
}
</script>

<style>
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
}
</style>
