<template>
  <div class="row" v-if="!isLoading()">
    <h1>{{ person.name }} {{ person.surname }}</h1>
    <p>Created by: {{ user.username }}</p>
    <div class="col">
      <div>
        <div class="row" v-if="ratings">
          <div class="col">
            <p>Hot: {{ avg_rating.hot }}</p>
            <p>Crazy: {{ avg_rating.crazy }}</p>
            <p>Nice: {{ avg_rating.nice }}</p>
          </div>
          <div class="col">
            <p>Score: {{ avg_rating.score.toFixed(1) }}</p>
          </div>
        </div>
        <div v-else>
          <p>Be the first to rate this person!</p>
        </div>
      </div>
      <div>
        <h3>Rating</h3>
        <div v-if="isLoggedIn">
          <div v-if="is_rated && !edit">
            <p>Your rating:</p>
            <PersonRating :rating="new_rating" @edit="edit = true" />
          </div>
          <div v-else>
            <p v-if="edit">Change your rating:</p>
            <p v-else>Rate this person:</p>
            <RatePerson
              :edit="edit"
              :rated="is_rated"
              :rating="new_rating"
              @update="updateView"
              @cancel="edit = false"
            />
          </div>
        </div>
        <div v-else>
          <p>You need to be logged in to rate people</p>
          <button class="btn btn-primary" @click="router.push('/login')">Login</button>
        </div>
      </div>
    </div>
    <div class="col">
      <PersonRatingList :ratings="ratings" />
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
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getPerson } from '@/api/person'
import { getUser, getUserPersonRating } from '@/api/user'

import type { Ref } from 'vue'
import type { Person } from '@/api/types/person'
import type { Rating, RatingNoID } from '@/api/types/rating'
import type { User } from '@/api/types/user'
import { getAuth, onAuthStateChanged } from 'firebase/auth'
import { getAverageRating, getPersonRatings } from '@/api/rating'

const loading = ref({
  person: true,
  ratings: true,
  avg_rating: true,
  user: true,
  is_rated: true
})

const route = useRoute()
const router = useRouter()

const edit = ref(false)
const is_rated = ref(false)

const person: Ref<Person> = ref({} as Person)
const ratings: Ref<Rating[]> = ref([])
const user: Ref<User> = ref({} as User)
const avg_rating = ref({
  score: 0,
  hot: 0,
  nice: 0,
  crazy: 0
})
const new_rating: Ref<RatingNoID> = ref({
  person_id: Number(route.params.person_id),
  user_id: 0,
  score: 0,
  hot: 5,
  nice: 5,
  crazy: 5,
  comment: ''
})

const isLoggedIn = ref(false)

function updateView() {
  edit.value = false
  is_rated.value = true

  loading.value.avg_rating = true
  loading.value.ratings = true
  loading.value.is_rated = true

  getAverageRating(Number(route.params.person_id))
    .then((api_rating) => {
      avg_rating.value.score = api_rating.score
      avg_rating.value.hot = api_rating.hot
      avg_rating.value.nice = api_rating.nice
      avg_rating.value.crazy = api_rating.crazy
    })
    .finally(() => {
      loading.value.avg_rating = false
    })

  getPersonRatings(Number(route.params.person_id))
    .then((api_ratings) => {
      ratings.value = api_ratings
    })
    .finally(() => {
      loading.value.ratings = false
    })

  getUserPersonRating(user.value.id, person.value.id)
    .then((user_person_rating) => {
      if (user_person_rating) {
        is_rated.value = true
        new_rating.value = user_person_rating
      }
    })
    .finally(() => {
      loading.value.is_rated = false
    })
}

let auth: any
onMounted(() => {
  getAverageRating(Number(route.params.person_id))
    .then((api_rating) => {
      avg_rating.value.score = api_rating.score
      avg_rating.value.hot = api_rating.hot
      avg_rating.value.nice = api_rating.nice
      avg_rating.value.crazy = api_rating.crazy
    })
    .finally(() => {
      loading.value.avg_rating = false
    })

  getPersonRatings(Number(route.params.person_id))
    .then((api_ratings) => {
      ratings.value = api_ratings
    })
    .finally(() => {
      loading.value.ratings = false
    })

  getPerson(Number(route.params.person_id))
    .then((api_person) => {
      person.value = api_person

      getUser(person.value.user_id)
        .then((api_user) => {
          user.value = api_user

          getUserPersonRating(user.value.id, person.value.id)
            .then((user_person_rating) => {
              if (user_person_rating) {
                is_rated.value = true
                new_rating.value = user_person_rating
              }
            })
            .finally(() => {
              loading.value.is_rated = false
            })
        })
        .finally(() => {
          loading.value.user = false
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

function isLoading() {
  return Object.values(loading.value).some((value) => value)
}
</script>
