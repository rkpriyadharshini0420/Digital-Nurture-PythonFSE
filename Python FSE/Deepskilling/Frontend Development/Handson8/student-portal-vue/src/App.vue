<script setup>
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
</script>

<template>
  <div id="app">
    <!-- Header component displays across all pages -->
    <Header />
    
    <!-- RouterView is the outlet for your page components -->
    <main class="page-container">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
#app {
  font-family: Arial, sans-serif;
  max-width: 1200px;
  margin: 0 auto;
}

.page-container {
  padding: 2rem;
}
</style>