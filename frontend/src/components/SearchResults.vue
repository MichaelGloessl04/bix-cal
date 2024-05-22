<template>
  <ul class="search-results" v-if="search_term">
    <li>
      <div @click="router.push('/add-person')">
        <i class="bi bi-person-plus"></i> Add new person
      </div>
    </li>
    <li v-if="loading">
      <div>Loading...</div>
    </li>
    <li v-else-if="results" v-for="person in props.results" :key="person.id">
      <PersonCard :person="person" @click="goToPerson(person)" />
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

function goToPerson(person: Person) {
  router.push(`/person/${person.id}`)
}
</script>
