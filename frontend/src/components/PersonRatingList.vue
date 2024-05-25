<template>
  <div>
    <h2>Person Ratings</h2>
    <div v-if="ratings">
      <ul>
        <li v-for="rating in ratings" :key="rating.id">
          <RatingCard :rating="rating" />
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
defineProps(['ratings'])
</script>
