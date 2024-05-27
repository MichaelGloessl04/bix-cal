<template>
  <div class="table-container">
    <table class="table table-dark table-striped table-hover table-borderless">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Score</th>
          <th scope="col">Hot</th>
          <th scope="col">Nice</th>
          <th scope="col">Crazy</th>
        </tr>
      </thead>
      <tbody v-if="people.length > 0">
        <tr v-for="person in people" :key="person.id">
          <PeopleListItem :person="person" />
        </tr>
      </tbody>
      <tbody v-else>
        <tr>
          <td>No Results.</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import PeopleListItem from './PeopleTableItem.vue'

import type { Person } from '@/api/types/person'

defineProps({
  people: {
    type: Array<Person>,
    required: true
  }
})
</script>

<style scoped>
.table-container {
  border-radius: 5px;
  box-shadow:
    11px 11px 18px #202428,
    -11px -11px 18px #2e343a;
}
</style>
