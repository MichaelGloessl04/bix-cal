<template>
    <div class="hover-box" v-if="add_window" >
        <h2>Quick Add Person</h2><br>
        <p class="close" @click="close_add_window">
            <i class="bi bi-x-circle-fill"></i>
        </p>
        <PersonAdd @submit="close_add_window"/>
    </div>
    <div class="screen-cover" v-if="add_window"></div>
</template>

<script setup lang="ts">
import PersonAdd from '@/components/PersonAdd.vue';

defineProps(['add_window']);
const emits = defineEmits(['close-add-window']);

function close_add_window() {
    emits('close-add-window');
}
</script>

<style scoped>
.close {
    position: absolute;
    top: 0;
    right: 0;
    padding: 0.5rem;
    cursor: pointer;
    width: fit-content;
}

.screen-cover {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6);
}
</style>