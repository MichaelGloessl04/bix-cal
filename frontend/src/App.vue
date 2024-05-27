<template>
  <div id="app">
    <header>
      <nav class="navbar navbar-expand-md navbar-dark bg-dark">
        <div class="container-fluid">
          <router-link to="/" class="navbar-brand">Bixcal</router-link>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <router-link to="/" class="nav-link">Home</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/people" class="nav-link">People</router-link>
              </li>
              <li v-if="isLoggedIn" class="nav-item">
                <router-link to="/add-person" class="nav-link">Add Person</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/about" class="nav-link">About</router-link>
              </li>
              <li v-if="!isLoggedIn" class="nav-item">
                <router-link to="/login" class="nav-link">Sign In</router-link>
              </li>
              <li v-if="!isLoggedIn" class="nav-item">
                <router-link to="/register" class="nav-link">Sign Up</router-link>
              </li>
              <li v-if="isLoggedIn" class="nav-item">
                <router-link to="/profile" class="nav-link">Profile</router-link>
              </li>
              <li v-if="isLoggedIn" class="nav-item">
                <router-link to="/logout" class="nav-link" @click="handleSignOut"
                  >Logout</router-link
                >
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
    <body>
      <div class="app"><RouterView /></div>
    </body>
  </div>
</template>

<script setup lang="ts">
import { getAuth, onAuthStateChanged, signOut } from 'firebase/auth'
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isLoggedIn = ref(false)

let auth: any
onMounted(() => {
  auth = getAuth()
  onAuthStateChanged(auth, (user) => {
    if (user) {
      isLoggedIn.value = true
    } else {
      isLoggedIn.value = false
    }
  })
})

function handleSignOut() {
  signOut(auth).then(() => {
    console.log('User signed out')
    router.push('/')
  })
}
</script>

<style>
.app {
  max-width: 1600px;
  margin: 0 auto;
  padding: 20px;
}
</style>
