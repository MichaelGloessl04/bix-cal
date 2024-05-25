<template>
  <div class="row hover-box">
    <h1>Log In</h1>
    <p><input type="email" placeholder="Email" v-model="email" /></p>
    <p><input type="password" placeholder="Password" v-model="password" /></p>
    <p v-if="errorMsg">{{ errorMsg }}</p>
    <p><button @click="login()">Submit</button></p>
    <p><router-link to="/register">Create Account</router-link></p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { getAuth, signInWithEmailAndPassword } from 'firebase/auth'
import { useRouter } from 'vue-router'
import type { UserNoID } from '@/api/types/user'
import { createUser } from '@/api/user'

const router = useRouter()

const email = ref('')
const password = ref('')
const errorMsg = ref('')

function addUserToDB() {
  const user: UserNoID = {
    person_id: 0,
    username: email.value.split('@')[0],
    email: email.value
  }
  createUser(user)
    .then(() => {
      console.log('User created in database')
    })
    .catch((error) => {
      console.error('Failed to create user in database', error)
    })
}

function login() {
  signInWithEmailAndPassword(getAuth(), email.value, password.value)
    .then(() => {
      console.log('User logged in')
      addUserToDB()
      router.push('/profile')
    })
    .catch((error) => {
      console.error('Failed to login', error)
      switch (error.code) {
        case 'auth/user-disabled':
          errorMsg.value = 'User disabled'
          break
        case 'auth/invalid-credential':
          errorMsg.value = 'Invalid credential'
          break
        case 'auth/wrong-password':
          errorMsg.value = 'Wrong password'
          break
        default:
          errorMsg.value = `Failed to login (${error.code})`
      }
    })
}
</script>
