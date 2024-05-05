<template>
    <div class="home-view">
        <h1>Bixcal</h1>
        <SearchBar />
    </div>
</template>

<script setup lang="ts">
import SearchBar from '@/components/SearchBar.vue';
</script>

<style scoped>
.home-view {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>
