<template>

<button @click="emits('changeRating')">Change rating</button>
</template>

<script setup lang="ts">
const emits = defineEmits(['changeRating'])
</script>