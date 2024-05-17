<template>
    <div class="about-container" v-html="about"></div>
</template>

<script setup lang="ts">
import { marked } from 'marked';
import { onMounted, ref } from 'vue';

import { getAbout } from '@/api/about';

const about = ref<string>('');

marked.setOptions({
    breaks: true,
    gfm: true,
});


onMounted(() => {
    getAbout().then(async (data) => {
        about.value = await marked(data);
    });
});
</script>
