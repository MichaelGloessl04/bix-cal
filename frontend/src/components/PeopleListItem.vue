<template>
    <td @click="router.push(`/person/${props.person.id}`)">
        {{ person.name }} {{ person.surname }}
    </td>
    <td class="vertical-align-middle">
        {{ score.score.toFixed(2) }}
    </td>
    <td>
        {{ score.hot.toFixed(2) }}
    </td>
    <td>
        {{ score.nice.toFixed(2) }}
    </td>
    <td>
        {{ score.crazy.toFixed(2) }}
    </td>
</template>

<script setup lang="ts">
import { onMounted, ref, type Ref } from 'vue';
import { useRouter } from 'vue-router';

import { getScore } from '@/api/score';
import type { Person } from '@/api/types/person';
import type { Scores } from '@/api/types/scores';

const router = useRouter()

const props = defineProps<{
    person: Person
}>()

const score: Ref<Scores> = ref({
    score: 0,
    hot: 0,
    nice: 0,
    crazy: 0
} as Scores)

onMounted(async () => {
    getScore(props.person.id)
        .then((data: Scores) => {
            score.value = data
        })
})
</script>
