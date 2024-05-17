<template>
    <div>
        <h1>Add new Person to the Database</h1>
        <p><input type="text" v-model="name" placeholder="Name"></p>
        <p><input type="text" v-model="surname" placeholder="Surname"></p>
        <p v-if="errorMsg">{{ errorMsg }}</p>
        <p><button @click="createPerson">Add Person</button></p>
    </div>
</template>

<script setup lang="ts">
import { addPerson } from '@/api/person';
import { getUser } from '@/api/user';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { getAuth } from 'firebase/auth';
import type { PersonNoID } from '@/api/types/person';

const router = useRouter();

const name = ref('');
const surname = ref('');
const errorMsg = ref('');


function createPerson() {
    const currentUser = getAuth().currentUser;
    if (!currentUser) {
        errorMsg.value = 'You need to be logged in to add a person';
        return;
    }
    getUser(currentUser.email!)
        .then((user) => {
            const newPerson: PersonNoID = {
                creator_id: user.id,
                name: name.value,
                surname: surname.value,
            }
            addPerson(newPerson)
                .then((person) => {
                    router.push(`/person/${person.id}`)
                })
                .catch((error) => {
                    switch (error.code) {
                        case 'permission-denied':
                            errorMsg.value = 'You do not have permission to add a person';
                            break;
                        default:
                            errorMsg.value = `An error occurred (${error.message})`;
                    }
                })
        })    
}
</script>