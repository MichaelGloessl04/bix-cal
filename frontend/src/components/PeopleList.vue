<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Overall Score</th>
          <th>Hot</th>
          <th>Nice</th>
          <th>Crazy</th>
        </tr>
      </thead>
      <tbody>
        <div v-if="people.length > 0">
          <tr v-for="person in people" :key="person.id">
            <PeopleListItem :person="person" />
          </tr>
        </div>
        <div v-else>
          <tr>
            <td>No Results.</td>
          </tr>
        </div>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import PeopleListItem from './PeopleListItem.vue'

import type { Person } from '@/api/types/person'

defineProps({
  people: {
    type: Array<Person>,
    required: true
  }
})
</script>
