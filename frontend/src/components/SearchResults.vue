<template>
    <ul class="search-results">
        <li v-for="person in props.results" :key="person.id">
            <PersonCard :person="person" @click="goToPerson(person)"/>
        </li>
    </ul>
</template>

<script setup lang="ts">
import PersonCard from '@/components/PersonCard.vue'

import { useRouter } from 'vue-router'

import type { Person } from '@/types/person'

const router = useRouter()

const props = defineProps(['results'])


function goToPerson(person: Person) {
    router.push(`/person/${person.id}`)
}
</script>

<style scoped>
.search-results {
    list-style-type: none;
    padding: 0;
}
.search-results li {
    background-color: white;
    color: black;
    padding: 0.5rem;
    cursor: pointer;
}
.search-results li:hover {
    background-color: rgb(220, 220, 220);
}
.search-results li:nth-child(odd) {
    background-color: rgb(240, 240, 240);
}
.search-results li:last-child {
    border-bottom-left-radius: 0.5rem;
    border-bottom-right-radius: 0.5rem;
}
</style>