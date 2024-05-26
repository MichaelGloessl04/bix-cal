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
import SearchResults from './SearchResults.vue'
import { ref, watch } from 'vue'
import { getPersons } from '@/api/person'
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
    getPersons(search_term.value).then((persons) => {
      results.value = persons
    })
    .catch((error) => {
      console.error(error)
    })
    .finally(() => {
      loading.value = false
    })
  }
}

function clearResults() {
  results.value.length = 0
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

<style scoped lang="scss">
$border-radius: 1rem;

.search-bar {
  width: 100%;
  margin-bottom: 0;
  margin-left: 0;
}

.search-bar input {
  width: 100%;
  padding: 0.5rem;
  padding-left: 1rem;
  font-size: 1.4rem;
  border: 0;
  border-radius: $border-radius;
}

.search-bar input:not(:placeholder-shown){
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
}

.search-bar input:focus {
  outline: none;
}

.search-container {
  padding: 0;
  width: 90%;
  max-width: 40rem;
  border-radius: $border-radius;
  box-shadow:  11px 11px 18px #191c1f,
             -11px -11px 18px #353c43
}
</style>