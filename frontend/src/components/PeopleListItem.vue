<template>
  <td @click="router.push(`/person/${props.person.id}`)">{{ person.name }} {{ person.surname }}</td>
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
import { onMounted, ref, type Ref } from 'vue'
import { useRouter } from 'vue-router'

import { getScores } from '@/api/person'
import type { Person } from '@/api/types/person'
import type { Scores } from '@/api/types/scores'

const router = useRouter()

const props = defineProps<{
  person: Person
}>()

const scores: Ref<Scores> = ref({
  score: 0,
  hot: 0,
  nice: 0,
  crazy: 0
} as Scores)

onMounted(() => {
  getScores(props.person.id)
    .then((data: Scores) => {
      scores.value = data
    })
    .catch((error) => {
      if (error.response.status === 404) {
        console.log('No scores found for person', props.person.id)
        scores.value = {
          score: 0,
          hot: 0,
          nice: 0,
          crazy: 0
        }
      }
    })
})
</script>
