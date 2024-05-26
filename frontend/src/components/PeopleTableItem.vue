<template>
  <td class="person-name" @click="router.push(`/person/${props.person.id}`)">
    {{ person.name }} {{ person.surname }}
  </td>
  <td>
    {{ scores.score.toFixed(2) }}
  </td>
  <td>
    {{ scores.hot.toFixed(2) }}
  </td>
  <td>
    {{ scores.nice.toFixed(2) }}
  </td>
  <td>
    {{ scores.crazy.toFixed(2) }}
  </td>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

import type { Person } from '@/api/types/person'
import type { Rating } from '@/api/types/rating'
import { getAverageRating } from '@/api/rating'

const router = useRouter()

const props = defineProps<{
  person: Person
}>()

const scores = ref({
  score: 0,
  hot: 0,
  nice: 0,
  crazy: 0
})

onMounted(() => {
  getAverageRating(props.person.id)
    .then((rating: Rating) => {
      scores.value.score = rating.score
      scores.value.hot = rating.hot
      scores.value.nice = rating.nice
      scores.value.crazy = rating.crazy
    })
    .catch((error) => {
      console.error(error)
    })
})
</script>

<style scoped>
.person-name {
  cursor: pointer;
}
</style>