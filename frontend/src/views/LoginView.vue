<template>
  <div class="row login-container">
    <h1>Sign In</h1>
    <p><input class="inp" type="email" placeholder="Email" v-model="email" /></p>
    <p><input class="inp" type="password" placeholder="Password" v-model="password" /></p>
    <p v-if="errorMsg">{{ errorMsg }}</p>
    <p><button class="btn btn-primary" @click="login()">Sing In</button></p>
    <p><router-link class="link" to="/register">Create Account</router-link></p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { getAuth, signInWithEmailAndPassword } from 'firebase/auth'
import { useRouter } from 'vue-router'

const router = useRouter()

const email = ref('')
const password = ref('')
const errorMsg = ref('')

function login() {
  signInWithEmailAndPassword(getAuth(), email.value, password.value)
    .then(() => {
      console.log('User logged in')
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
