<template>
  <div>
    <h2>Person Ratings</h2>
    <div v-if="entries.length > 0">
      <ul>
        <li v-for="entry in entries" :key="entry.id">
          <RatingCard :entry="entry" />
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No ratings yet.</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import RatingCard from '@/components/RatingCard.vue'
defineProps(['entries'])
</script>
