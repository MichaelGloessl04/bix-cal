<template>
  <div>
    <h1>People</h1>
    <PeopleList :people="people" />
  </div>
</template>

<script setup lang="ts">
import PeopleList from '@/components/PeopleList.vue'

import { onMounted, ref } from 'vue'

import { getPersons } from '@/api/person'
import type { Person } from '@/api/types/person'

const people = ref<Person[]>([])

async function getPeople() {
  people.value = await getPersons()
}

onMounted(getPeople)
</script>
