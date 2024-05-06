<template>
    <QuickAdd :add_window="add" @close-add-window="add = false"/>
    <div class="home-view">
        <h1>Bixcal</h1>
        <SearchBar @add="add = true"/>
    </div>
</template>

<script setup lang="ts">
import SearchBar from '@/components/SearchBar.vue';
import QuickAdd from '@/components/QuickAdd.vue';

import { ref } from 'vue';

const add = ref(false);

</script>

<style scoped>
.home-view {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-top: 20vh;
}

h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.search-bar {
    margin-top: 1rem;
}
</style>
