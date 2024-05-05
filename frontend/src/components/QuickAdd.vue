<template>
    <div class="hover-box" v-if="add_window" >
        <p class="close" @click="close_add_window">
            <i class="bi bi-x-circle-fill"></i>
        </p>
        <PersonAdd @submit="close_add_window"/>
    </div>
</template>

<script setup lang="ts">
import PersonAdd from '@/components/PersonAdd.vue';

const props = defineProps(['add_window']);
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
}</style>