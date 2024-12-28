<template>
  <div class="ratings-container">
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

<style scoped>
.ratings-container {
  margin-top: 20px;
}

.ratings-container h2 {
  margin-bottom: 10px;
}

.ratings-container ul {
  list-style-type: none;
  padding: 0;
}

.ratings-container li {
  margin-bottom: 10px;
}

.ratings-container p {
  margin: 0;
}

.ratings-container .rating {
  display: flex;
  justify-content: space-between;
}
</style>
