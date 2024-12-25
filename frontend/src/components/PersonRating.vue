<template>
  <div>
    <p>Hot: {{ rating.hot }}</p>
    <p>Crazy: {{ rating.crazy }}</p>
    <p>Nice: {{ rating.nice }}</p>
    <p v-if="rating.comment">Comment: {{ rating.comment }}</p>
  </div>
  <button class="btn btn-primary btn-sm" @click="emits('edit')">edit</button>
  <button class="btn btn-danger btn-sm" @click="emits('delete')">delete</button>
</template>

<script setup lang="ts">
defineProps(['rating', 'delete'])
const emits = defineEmits(['edit', 'delete'])
</script>
