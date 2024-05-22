<template>
  <div>
    <div>{{ props.person.name }} {{ props.person.surname }}</div>
    <div @click="open_quick_view">
      <i class="bi bi-eye-fill"></i>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps(['person'])

function open_quick_view() {
  /* TODO: Open quick view */
}
</script>
