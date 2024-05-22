<template>
  <div>
    <div>
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
import SearchResults from './SearchResults.vue'
import { ref, watch } from 'vue'
import { searchPersons } from '@/api/person'
import type { Ref } from 'vue'
import type { Person } from '@/api/types/person'

const emits = defineEmits(['add'])

const loading = ref(false)
const search_term = ref('')
const results: Ref<Person[]> = ref([])

async function search() {
  if (search_term.value === '') {
    results.value.length = 0
  } else {
    loading.value = true
    searchPersons(search_term.value)
      .then((response) => {
        clearResults()
        console.log(response)
        results.value = response
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
watch(
  () => results.value,
  () => {
    if (search_term.value === '') {
      clearResults()
    } else if (results.value.length === 0 && search_term.value !== '') {
      clearResults()
    }
  }
)
</script>
