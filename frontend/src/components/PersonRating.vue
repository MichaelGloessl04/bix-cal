<template>
  <div>
    <p>Hot: {{ rating.hot }}</p>
    <p>Crazy: {{ rating.crazy }}</p>
    <p>Nice: {{ rating.nice }}</p>
    <p v-if="rating.comment">Comment: {{ rating.comment }}</p>
  </div>
  <button class="btn btn-primary btn-sm" @click="emits('edit')">Change rating</button>
</template>

<script setup lang="ts">
defineProps(['rating'])
const emits = defineEmits(['edit'])
</script>
