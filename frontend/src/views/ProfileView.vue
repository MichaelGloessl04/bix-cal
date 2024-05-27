<template>
  <div v-if="!loading" class="profile-view">
    <h1>Profile</h1>
    <p>Username: {{ user.username }}</p>
    <p>Email: {{ user.email }}</p>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, type Ref } from 'vue'
import { getAuth } from 'firebase/auth'
import { getUserByEmail } from '@/api/user'
import type { User } from '@/api/types/user'

const auth = getAuth()
const user: Ref<User> = ref<User>({} as User)

const loading = ref(true)

onMounted(() => {
  const currentEmail = auth.currentUser?.email
  if (auth.currentUser && currentEmail) {
    getUserByEmail(currentEmail)
      .then((response) => {
        user.value = response
      })
      .catch((error) => {
        console.error(error)
      })
      .finally(() => {
        loading.value = false
      })
  }
})
</script>
