<template>
    <div class="search-container">
        <div class="search-bar">
            <input
            type="text"
            v-model="search_term"
            @keydown="search"
            placeholder="Search for a Person..."
            />
        </div>
        <SearchResults v-if="results.length > 0" :results="results" />
    </div>
</template>

<script setup lang="ts">
import SearchResults from './SearchResults.vue';

import axios from 'axios'

import { ref, watch} from 'vue'

import type { Ref } from 'vue'
import type { Person } from '@/types/person'

const search_term = ref('')
const results: Ref<Person[]> = ref([])


async function search() {
    results.value.push({ id: 0, name: 'Loading...', surname: '' })
    if (search_term.value === '') {
        results.value.length = 0
    } else {
        console.log(`searching for '${search_term.value}'...`)
        const params: { [key: string]: string } = {}
        params['search_term'] = search_term.value
        axios.get(`/api/person/`, { params: params })
            .then(response => {
                console.log(response)
                results.value = response.data
            })
            .catch(error => {
                console.error(error)
            })
            .finally(() => {
                console.log('search completed')
            })
    }
}

watch(search_term, search)
watch(() => results.value, () => {
    if (search_term.value === '') {
        results.value.length = 0
        console.log('cleared results')
    } else if (results.value.length === 0 && search_term.value !== '') {
        results.value.length = 0
        results.value.push({ id: 0, name: 'No results found', surname: '' })
    }
})
</script>

<style scoped>
.search-bar {
    display: flex;
    justify-content: center;
    margin: 1rem;
    margin-bottom: 0;
    width: 100%;
}

.search-bar input {
    width: 100%;
    padding: 0.5rem;
    font-size: 1rem;
    border: 0;
    border-radius: 0.5rem;
}

/* remove border radius if input is not empty */
.search-bar input:not(:placeholder-shown) {
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
}

.search-bar input:focus {
    outline: none;
}

.search-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 70%;
}

.search-container > * {
    width: 100%;
}


</style>
