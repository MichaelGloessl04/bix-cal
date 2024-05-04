<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import SearchBar from './components/SearchBar.vue'
</script>

<template>
  <div id="app">
      <header>
          <SearchBar />
          <nav>
              <RouterLink to="/">Home</RouterLink>
              <RouterLink to="/about">About</RouterLink>
          </nav>
      </header>
  </div>
  <RouterView />
</template>

<style scoped>

</style>
