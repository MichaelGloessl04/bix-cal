<template>
  <form @submit.prevent>
    <p>
      <span for="hot">Hot</span>
      <input id="hot" v-model="hot" type="range" min="1" max="10" />
      <span>{{ hot }}</span>
    </p>
    <p>
      <span for="crazy">Crazy</span>
      <input id="crazy" v-model="crazy" type="range" min="1" max="10" />
      <span>{{ crazy }}</span>
    </p>
    <p>
      <span for="nice">Nice</span>
      <input id="nice" v-model="nice" type="range" min="1" max="10" />
      <span>{{ nice }}</span>
    </p>
    <p>
      <input id="comment" v-model="comment" type="message" placeholder="Comment" maxlength="20" />
      <span>{{ comment.length }}/20</span>
    </p>
    <button class="btn btn-secondary btn-sm" v-if="edit" @click="emits('cancel')">Cancel</button>
    <button id="submit" class="btn btn-primary btn-sm" @click="submit">Submit</button>
  </form>
</template>

<script setup lang="ts">
import { createRating, editRating } from '@/api/rating'
import type { RatingNoID } from '@/api/types/rating'
import { getUserByEmail } from '@/api/user'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getAuth } from 'firebase/auth'

const route = useRoute()
const router = useRouter()

const emits = defineEmits(['update', 'cancel', 'refresh'])
const props = defineProps(['edit', 'rated', 'rating'])

const score = ref(0)
const hot = ref(5)
const crazy = ref(5)
const nice = ref(5)
const comment = ref('')

const submit = () => {
  console.log(hot.value, crazy.value, nice.value, comment.value)
  const currentUser = getAuth().currentUser
  if (!currentUser) {
    router.push('/login')
    return
  }

  getUserByEmail(currentUser.email!).then((user) => {
    if (!props.edit) {
      const newRating: RatingNoID = {
        person_id: Number(route.params.person_id),
        user_id: user.id,
        score: (hot.value + crazy.value + nice.value) / 3,
        hot: hot.value,
        crazy: crazy.value,
        nice: nice.value,
        comment: comment.value
      }
      createRating(newRating)
        .then(() => {
          emits('refresh')
        })
    } else {
      const updatedRating = {
        ...props.rating,
        hot: hot.value,
        crazy: crazy.value,
        nice: nice.value,
        comment: comment.value
      }
      editRating(props.rating.id, updatedRating)
        .then(() => {
          emits('refresh')
        })
    }
  })
}

onMounted(() => {
  if (props.rated) {
    score.value = props.rating.score
    hot.value = props.rating.hot
    crazy.value = props.rating.crazy
    nice.value = props.rating.nice
    comment.value = props.rating.comment
  }
})
</script>
