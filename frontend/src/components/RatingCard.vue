<template>
  <div class="row">
    <div class="row">
      <span>{{ author.username }}</span>
    </div>
    <div class="row">
      <span>{{ entry.hot + entry.nice + (4 - entry.crazy) }}</span>
    </div>
    <div class="row">
      <span class="col">{{ entry.hot }}</span>
      <span class="col">{{ entry.nice }}</span>
      <span class="col">{{ entry.crazy }}</span>
    </div>
    <div class="row">
      <span>{{ entry.comment }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Entry } from '@/api/types/entry'
import type { User } from '@/api/types/user'
import { getUserByID } from '@/api/user'
import { onMounted, ref, type Ref } from 'vue'

const props = defineProps<{ entry: Entry }>()

const author: Ref<User> = ref({} as User)

onMounted(() => {
  getUserByID(props.entry.author_id).then((user) => {
    author.value = user
  })
})
</script>
