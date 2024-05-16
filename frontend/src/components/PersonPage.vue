<template>
    <div class="person-view">
        <h1>{{ person.name }} {{ person.surname }}</h1>
        <p>Score: {{ scores.score }}</p>
        <p>Hot: {{ scores.hot }}</p>
        <p>Nice: {{ scores.nice }}</p>
        <p>Crazy: {{ scores.crazy }}</p>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

import { getPerson } from '@/api/person';
import { getScore } from '@/api/score';

import type { Ref } from 'vue';
import type { Person } from '@/api/types/person';
import type { Scores } from '@/api/types/scores';

const props = defineProps(['person_id'])

const person: Ref<Person> = ref({} as Person)
const scores: Ref<Scores> = ref({} as Scores)

onMounted(async () => {
    person.value = await getPerson(props.person_id)
    scores.value = await getScore(props.person_id)
})
</script>