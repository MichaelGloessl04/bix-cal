<template>
    <div class="search-bar">
        <input
        type="text"
        v-model="search_term"
        @input="search"
        placeholder="Search for a movie..."
        />
    </div>
</template>

<script setup lang="ts">
import axios from 'axios'
import { ref, watch, type Ref } from 'vue'
import { useRouter } from 'vue-router'
import { type Person } from '../scripts/person'

const search_term = ref('')
const results: Ref<Person[]> = ref([])
const typing = ref(false)
const router = useRouter()

async function search() {
    typing.value = true
    if (typing.value) {
        return
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
    typing.value = false
    if (search_term.value === '') {
        return
    }
    console.log('searching...')
    const params = new URLSearchParams()
    params.append('search_term', search_term.value)
    axios.get(`/api/person/search`, { params })
        .then(response => {
            router.push({ name: 'SearchResults', query: { search_term: search_term.value } })
        })
        .catch(error => {
            console.error(error)
        })
        .finally(() => {
            console.log('search complete')
            console.log(results.value)
        })
}

watch(search_term, search)
</script>
