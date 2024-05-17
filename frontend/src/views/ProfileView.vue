<template>
    <div class="profile-view">
        <h1>Profile</h1>
        <p>Username: {{ user.username }}</p>
        <p>Email: {{ user.email }}</p>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, type Ref } from 'vue'
import { getAuth } from 'firebase/auth'
import { getUser } from '@/api/user'
import type { User } from '@/api/types/user';

const auth = getAuth()
const user: Ref<User> = ref<User>({} as User)


onMounted(() => {
    const currentEmail = auth.currentUser?.email
    if (auth.currentUser && currentEmail) {
        getUser(currentEmail)
            .then((response) => {
                user.value = response
            })
            .catch((error) => {
                console.error(error)
            })
    }
})
</script>
