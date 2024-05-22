<template>
  <div class="row" v-if="!isLoading()">
    <h1>{{ person.name }} {{ person.surname }}</h1>
    <p>Created by: {{ creator.username }}</p>
    <div class="col">
      <div>
        <div class="row" v-if="entries.length > 0">
          <div class="col">
            <p>Hot: {{ scores.hot }}</p>
            <p>Crazy: {{ scores.crazy }}</p>
            <p>Nice: {{ scores.nice }}</p>
          </div>
          <div class="col">
            <p>Score: {{ scores.score.toFixed(2) }}</p>
          </div>
        </div>
        <div v-else>
          <p>Be the first to rate this person!</p>
        </div>
      </div>
      <div>
        <h3>Rating</h3>
        <div v-if="isLoggedIn">
          <div v-if="rated && !edit">
            <p>Your rating:</p>
            <PersonRating :rating="entry" @edit="edit = true" />
          </div>
          <div v-else>
            <p v-if="edit">Change your rating:</p>
            <p v-else>Rate this person:</p>
            <RatePerson :edit="edit" :rated="rated" :entry="entry" @cancel="edit = false" />
          </div>
        </div>
        <div v-else>
          <p>You need to be logged in to rate people</p>
          <button @click="router.push('/login')">Login</button>
        </div>
      </div>
    </div>
    <div class="col">
      <PersonRatingList :entries="entries" />
    </div>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script setup lang="ts">
import PersonRatingList from '@/components/PersonRatingList.vue'
import RatePerson from '@/components/RatePerson.vue'
import PersonRating from '@/components/PersonRating.vue'
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getPerson, getScores, getEntries } from '@/api/person'
import { getRating, getUserByID, hasRated } from '@/api/user'

import type { Ref } from 'vue'
import type { Person } from '@/api/types/person'
import type { Scores } from '@/api/types/scores'
import type { Entry, EntryNoID } from '@/api/types/entry'
import type { User } from '@/api/types/user'
import { getAuth, onAuthStateChanged } from 'firebase/auth'

const loading = ref({
  person: true,
  entries: true,
  scores: true,
  creator: true,
  rated: true
})

const route = useRoute()
const router = useRouter()

const edit = ref(false)
const rated = ref(false)

const person: Ref<Person> = ref({} as Person)
const entries: Ref<Entry[]> = ref([])
const scores: Ref<Scores> = ref({} as Scores)
const creator: Ref<User> = ref({} as User)
const entry: Ref<EntryNoID> = ref({
  person_id: Number(route.params.person_id),
  author_id: 0,
  hot: 5,
  crazy: 5,
  nice: 5,
  comment: ''
})

const isLoggedIn = ref(false)

let auth: any
onMounted(() => {
  getScores(Number(route.params.person_id))
    .then((response) => {
      scores.value = response
    })
    .finally(() => {
      loading.value.scores = false
    })
  getEntries(Number(route.params.person_id))
    .then((response) => {
      entries.value = response
    })
    .finally(() => {
      loading.value.entries = false
    })
  getPerson(Number(route.params.person_id))
    .then((response) => {
      person.value = response
      getUserByID(person.value.creator_id)
        .then((user) => {
          creator.value = user
          hasRated(user.id, person.value.id)
            .then((response) => {
              rated.value = response
              getRating(user.id, person.value.id)
                .then((response) => {
                  entry.value = response
                })
                .finally(() => {
                  loading.value.rated = false
                })
            })
            .finally(() => {
              loading.value.rated = false
            })
        })
        .finally(() => {
          loading.value.creator = false
        })
    })
    .finally(() => {
      loading.value.person = false
    })
  auth = getAuth()
  onAuthStateChanged(auth, (user) => {
    if (user) {
      isLoggedIn.value = true
    } else {
      isLoggedIn.value = false
    }
  })
})

watch(rated, () => {
  console.log('rated: ', rated.value)
})
watch(edit, () => {
  console.log('edit: ', edit.value)
})

function isLoading() {
  return Object.values(loading.value).some((value) => value)
}
</script>
