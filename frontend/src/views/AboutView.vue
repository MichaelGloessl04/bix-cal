<template>
    <div class="about-container" v-html="about"></div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { marked } from 'marked';
import { onMounted, ref } from 'vue';

const about = ref<string>('');

marked.setOptions({
    breaks: true,
    gfm: true,
});


function getAboutContent() {
    axios.get('/api/')
        .then(async (response) => {
            about.value = await marked(response.data);
        })
        .catch((error) => {
            console.error(error);
        });
}

onMounted(() => {
    getAboutContent();
});
</script>

<style>
.about-container {
    width: 80%;
    margin: 0 auto;
}
</style>
