<template>
<button @click="emits('edit')">Change rating</button>
</template>

<script setup lang="ts">
const emits = defineEmits(['edit'])
</script>