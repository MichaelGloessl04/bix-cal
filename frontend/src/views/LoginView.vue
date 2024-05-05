<template>
    <div class="hover-box">
        <h1>Login</h1>
        <form>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" v-model="username">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" v-model="password">
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="remember">
                <label class="form-check
                -label" for="remember">Remember me</label>
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
        </form>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const username = ref('')
const password = ref('')
const remember = ref(false)

const login = () => {
    console.log('Login clicked')
}
</script>

<style scoped>
h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

button {
    margin-top: 1rem;
}

.hover-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    top: 40%;
}
</style>
