<template>
    <div class="row hover-box">
        <h1>Log In</h1>
        <p><input type="email" placeholder="Email" v-model="email" /></p>
        <p><input type="password" placeholder="Password" v-model="password" /></p>
        <p v-if="errorMsg">{{ errorMsg }}</p>
        <p><button @click="login()">Submit</button></p>
        <p><button @click="loginWithGoogle()">Login with Google</button></p>
        <p><router-link to="/register">Create Account</router-link></p>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { getAuth, signInWithEmailAndPassword, GoogleAuthProvider, signInWithPopup } from 'firebase/auth'
import { useRouter } from 'vue-router';

const router = useRouter()

const email = ref('')
const password = ref('')
const errorMsg = ref('')

function login() {
    signInWithEmailAndPassword(getAuth(), email.value, password.value)
        .then(() => {
            console.log('User registered')
            router.push('/')
        })
        .catch((error) => {
            console.error('Failed to login', error)
            switch (error.code) {
                case 'auth/invalid-email':
                    errorMsg.value = 'Invalid email'
                    break
                case 'auth/user-disabled':
                    errorMsg.value = 'User disabled'
                    break
                case 'auth/user-not-found':
                    errorMsg.value = 'User not found'
                    break
                case 'auth/wrong-password':
                    errorMsg.value = 'Wrong password'
                    break
                default:
                    errorMsg.value = 'Failed to login'
            }
        })
}

function loginWithGoogle() {
    console.log('Register with Google')
    const provider = new GoogleAuthProvider()
    signInWithPopup(getAuth(), provider)
        .then(() => {
            console.log('User registered with Google')
            router.push('/')
        })
}
</script>