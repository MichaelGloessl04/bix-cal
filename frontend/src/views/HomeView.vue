<template>
  <div class="home-container">
    <h1>Bixcal</h1>
    <SearchBar @add="add = true" />
  </div>
</template>

<script setup lang="ts">
import SearchBar from '@/components/SearchBar.vue'

import { ref } from 'vue'

const add = ref(false)
</script>

<style scoped>
h1 {
  font-size: 4rem;
  margin-bottom: 1rem;
  text-align: center;
}

.home-container {
  display: flex; 
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 40vh;
}
</style>
