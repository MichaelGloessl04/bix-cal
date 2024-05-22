<template>
  <div>
    <p>Hot: {{ rating.hot }}</p>
    <p>Crazy: {{ rating.crazy }}</p>
    <p>Nice: {{ rating.nice }}</p>
    <p>Comment: {{ rating.comment }}</p>
  </div>
  <button @click="emits('edit')">Change rating</button>
</template>

<script setup lang="ts">
defineProps(['rating'])
const emits = defineEmits(['edit'])
</script>
