<template>
    <div class="profile-view">
        <h1>Profile</h1>
        <p>Email: {{  }}</p>
        <p>Display Name: {{ displayName }}</p>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { getAuth } from 'firebase/auth'

import { getUser } from '@/api/api_calls'

const auth = getAuth()
const user = ref(auth.currentUser)

function getUser() {

}
