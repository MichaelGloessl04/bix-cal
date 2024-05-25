<template>
  <div class="row">
    <div class="row">
      <span>{{ user.username }}</span>
    </div>
    <div class="row">
      <span>{{ rating.score }}</span>
    </div>
    <div class="row">
      <span class="col">{{ rating.hot }}</span>
      <span class="col">{{ rating.nice }}</span>
      <span class="col">{{ rating.crazy }}</span>
    </div>
    <div class="row">
      <span>{{ rating.comment }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { User } from '@/api/types/user'
import { getUser } from '@/api/user'
import { onMounted, ref, type Ref } from 'vue'

const props = defineProps(['rating'])

const user: Ref<User> = ref({} as User)

onMounted(() => {
  getUser(props.rating.user_id).then((api_user) => {
    user.value = api_user
  })
})
</script>
