<template>
    <ul class="search-results" v-if="search_term">
        <li>
            <div @click="emits('add')">
                <i class="bi bi-person-plus"></i> Add new person
            </div>
        </li>
        <li v-if="loading">
            <div>Loading...</div>
        </li>
        <li v-else-if="results" v-for="person in props.results" :key="person.id">
            <PersonCard :person="person" @click="goToPerson(person)"/>
        </li>
        <li v-else>
            <div>No results</div>
        </li>
    </ul>
</template>

<script setup lang="ts">
import PersonCard from '@/components/PersonCard.vue'
import { useRouter } from 'vue-router'
import type { Person } from '@/api/types/person'

const router = useRouter()
const props = defineProps(['results', 'loading', 'search_term'])
const emits = defineEmits(['add'])


function goToPerson(person: Person) {
    router.push(`/person/${person.id}`)
}
</script>

<style scoped lang="scss">
$border-radius: 1rem;

.search-results {
    width: 100%;
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.search-results li {
    background-color: white;
    color: black;
    padding: 0.5rem;
    cursor: pointer;
}

.search-results li:hover,
.search-results li:nth-child(odd):hover {
    background-color: rgb(220, 220, 220);
}

.search-results li:nth-child(odd) {
    background-color: rgb(245, 245, 245);
}

.search-results li:last-child {
    border-bottom-left-radius: $border-radius;
    border-bottom-right-radius: $border-radius;
}
</style>