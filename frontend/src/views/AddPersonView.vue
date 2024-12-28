<template>
  <div class="add-container">
    <h1>Add Person</h1>
    <p class="sub-title">Add a new Person to the Database.</p>
    <p><input type="text" v-model="name" placeholder="Name" /></p>
    <p><input type="text" v-model="surname" placeholder="Surname" /></p>
    <p v-if="errorMsg">{{ errorMsg }}</p>
    <p><button class="btn btn-primary" @click="submit">Add Person</button></p>
  </div>
</template>

<script setup lang="ts">
import { createPerson } from '@/api/person'
import { getUserByEmail } from '@/api/user'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { getAuth } from 'firebase/auth'
import type { PersonNoID } from '@/api/types/person'

const router = useRouter()

const name = ref('')
const surname = ref('')
const errorMsg = ref('')

function submit() {
  const currentUser = getAuth().currentUser
  if (!currentUser) {
    errorMsg.value = 'You need to be logged in to add a person'
    return
  }
  getUserByEmail(currentUser.email!).then((user) => {
    const newPerson: PersonNoID = {
      user_id: user.id,
      name: name.value,
      surname: surname.value,
      image_url: ''
    }
    createPerson(newPerson)
      .then((person) => {
        router.push(`/person/${person.id}`)
      })
      .catch((error) => {
        switch (error.code) {
          case 'permission-denied':
            errorMsg.value = 'You do not have permission to add a person'
            break
          default:
            errorMsg.value = `An error occurred (${error.message})`
        }
      })
  })
}
</script>

<style>
h1 {
  padding: 0;
  margin-bottom: 0;
}

.sub-title {
  padding: 0%;
  margin-top: 0;
}

.add-container {
  margin: 0 auto;
  margin-top: 10%;
  width: 300px;
  padding: 20px;
  box-shadow:
    11px 11px 18px #202428,
    -11px -11px 18px #2e343a;
  border-radius: 1rem;
}
</style>
