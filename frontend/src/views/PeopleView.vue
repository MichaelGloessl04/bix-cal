<template>
    <div class="people-view">
        <h1>People</h1>
        <PeopleList :people="people" />
    </div>
</template>

<script setup lang="ts">
import PeopleList from '@/components/PeopleList.vue';

import { onMounted, ref } from 'vue';

import { getPersons } from '@/scripts/api_calls';
import type { Person } from '@/types/person';

const people = ref<Person[]>([]);

async function getPeople() {
    people.value = await getPersons();
}

onMounted(getPeople);
</script>

<style>
.people-view {
    width: 80%;
    margin: 0 auto;
}
</style>