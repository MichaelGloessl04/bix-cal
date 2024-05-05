<template>
    <div class="person-card">
        {{ props.person.name }} {{ props.person.surname }}
    </div>
</template>

<script setup lang="ts">
const props = defineProps(['person'])
</script>
