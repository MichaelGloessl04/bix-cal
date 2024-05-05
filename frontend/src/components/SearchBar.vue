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
        <SearchResults
            :results="results"
            :loading="loading"
            :search_term="search_term"
            @add="emits('add')"
        />
    </div>
</template>

<script setup lang="ts">
import SearchResults from './SearchResults.vue';

import axios from 'axios'

import { ref, watch} from 'vue'

import type { Ref } from 'vue'
import type { Person } from '@/types/person'

const emits = defineEmits(['add'])

const loading = ref(false)
const search_term = ref('')
const results: Ref<Person[]> = ref([])


async function search() {
    if (search_term.value === '') {
        results.value.length = 0
    } else {
        console.log(`searching for '${search_term.value}'...`)
        const params: { [key: string]: string } = {}
        params['search_term'] = search_term.value
        axios.get(`/api/person/`, { params: params })
            .then(response => {
                clearResults()
                loading.value = true
                console.log(response)
                results.value = response.data
            })
            .catch(error => {
                loading.value = false
                console.error(error)
            })
            .finally(() => {
                loading.value = false
                console.log('search completed')
            })
    }
}


function clearResults() {
    results.value.length = 0
    console.log('cleared results')
}


watch(search_term, search)
watch(() => results.value, () => {
    if (search_term.value === '') {
        clearResults()
    } else if (results.value.length === 0 && search_term.value !== '') {
        clearResults()
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
    font-size: 1.4rem;
    border: 0;
    border-radius: 1rem;
}

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
