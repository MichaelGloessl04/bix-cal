<template>
  <div class="row">
    <div class="col">{{ props.person.name }} {{ props.person.surname }}</div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps(['person'])

function open_quick_view() {
  /* TODO: Open quick view */
}
</script>
