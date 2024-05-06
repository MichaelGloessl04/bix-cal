<template>
    <div class="row">
        <div class="col-sm-3">
            {{ props.person.name }} {{ props.person.surname }}
        </div>
        <div class="col-sm text-end quick-view" @click="">
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

<style scoped>
.quick-view {
    display: none;
}

.row:hover .quick-view {
    display: block;
}
</style>
