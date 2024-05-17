<template>
    <div>
        <h1>{{ person.name }} {{ person.surname }}</h1>
        <p>Created by: {{ creator.username }}</p>
        <div v-if="entries.length > 0">
            <p>Score: {{ scores.score }}</p>
            <p>Hot: {{ scores.hot }}</p>
            <p>Crazy: {{ scores.crazy }}</p>
            <p>Nice: {{ scores.nice }}</p>
        </div>
        <div v-else>
            <p>Be the first to rate this person!</p>
        </div>
    </div>
    <div v-if="getAuth().currentUser">
        <RatePerson v-if="!rated" :rated="rated" @change-rating="rated = !rated"/>
        <PersonRating v-else @change-rating="rated = !rated" />
    </div>
</template>

<script setup lang="ts">
import RatePerson from '@/components/RatePerson.vue'
import PersonRating from '@/components/PersonRating.vue'
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getPerson, getScores, getEntries } from '@/api/person';
import { getUserByID, hasRated } from '@/api/user';

import type { Ref } from 'vue';
import type { Person } from '@/api/types/person';
import type { Scores } from '@/api/types/scores';
import type { Entry } from '@/api/types/entry';
import type { User } from '@/api/types/user';
import { getAuth } from 'firebase/auth';

const route = useRoute()

const rated = ref(false)

const person: Ref<Person> = ref({} as Person)
const entries: Ref<Entry[]> = ref([]) 
const scores: Ref<Scores> = ref({} as Scores)

const creator: Ref<User> = ref({} as User)

onMounted(async () => {
    person.value = await getPerson(Number(route.params.person_id))
    scores.value = await getScores(Number(route.params.person_id))
    entries.value = await getEntries(Number(route.params.person_id))
    getUserByID(person.value.creator_id)
        .then((user) => {
            creator.value = user
            
            hasRated(user.id, person.value.id)
                .then((response) => {
                    console.log(response)
                    rated.value = response
                })
        })
})
</script>