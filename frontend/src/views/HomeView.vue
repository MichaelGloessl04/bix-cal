<template>
    <div>
        <h1>Bixcal</h1>
        <SearchBar @add="add = true"/>
    </div>
</template>

<script setup lang="ts">
import SearchBar from '@/components/SearchBar.vue';

import { ref } from 'vue';

const add = ref(false);
</script>
