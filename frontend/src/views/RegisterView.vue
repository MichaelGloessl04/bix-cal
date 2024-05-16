<template>
    <div class="row hover-box">
        <h1>Create an Account</h1>
        <p><input type="text" placeholder="Username" v-model="username" /></p>
        <p><input type="email" placeholder="Email" v-model="email" /></p>
        <p><input type="password" placeholder="Password" v-model="password" /></p>
        <p v-if="errorMsg">{{ errorMsg }}</p>
        <p><button @click="register()">Register</button></p>
        <p><button @click="registerWithGoogle()">Register with Google</button></p>
        <p><router-link to="/login">Already have an account?</router-link></p>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { getAuth, createUserWithEmailAndPassword, GoogleAuthProvider, signInWithPopup } from 'firebase/auth'
import { useRouter } from 'vue-router';
import { createUser } from '@/api/user';
import type { UserNoID } from '@/api/types/user';

const router = useRouter()
const username = ref('')
const email = ref('')
const password = ref('')
const errorMsg = ref('')

function register() {
    createUserWithEmailAndPassword(getAuth(), email.value, password.value)
        .then(() => {
            console.log('User registered')
            const user: UserNoID = {
                username: username.value,
                email: email.value,
            }
            createUser(user)
                .then(() => {
                    console.log('User created in database')
                })
                .catch((error) => {
                    if (error.code === 'User already exists')
                        console.log('User already exists in database')
                    else
                        console.error('Failed to create user in database', error)
                })
            router.push('/')
        })
        .catch((error) => {
            console.error('Failed to register', error)
            switch (error.code) {
                case 'auth/email-already-in-use':
                    errorMsg.value = 'Email already in use'
                    break
                case 'auth/invalid-email':
                    errorMsg.value = 'Invalid email'
                    break
                case 'auth/weak-password':
                    errorMsg.value = 'Weak password'
                    break
                default:
                    errorMsg.value = 'Failed to register'
            }
        })
}

function registerWithGoogle() {
    console.log('Register with Google')
    const provider = new GoogleAuthProvider()
    signInWithPopup(getAuth(), provider)
        .then(() => {
            console.log('User registered with Google')
            router.push('/')
        })
}
</script>
