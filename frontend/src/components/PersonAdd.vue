<template>
    <div class="person-add" @submit.prevent="submit">
        <form>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" v-model="person.name" class="form-control" id="name" placeholder="Name" required/>
            </div>
            <div class="form-group">
                <label for="surname">Surname</label>
                <input type="text" v-model="person.surname" class="form-control" id="surname" placeholder="Surname" required/>
            </div>
            <button type="submit" class="btn btn-primary">Add</button>
        </form>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import { addPerson } from '@/api/api_calls'

import type { Ref } from 'vue'
import type { PersonNoID } from '@/types/person'

const emits = defineEmits(['submit'])

const person: Ref<PersonNoID> = ref({
    name: '',
    surname: ''
})

const router = useRouter()


function submit() {
    if (person.value.name && person.value.surname) {
        addPerson(person.value)
        emits('submit')
    } else {
        alert('Please fill in all fields')
    }
}
</script>

<style scoped>
.person-add form {
    width: 80%;
}

.person-add .form-group {
    margin-bottom: 1rem;
}

.person-add button {
    width: 100%;
}

.person-add input {
    width: 100%;
}

.person-add label {
    font-weight: bold;
}

.person-add button {
    margin-top: 1rem;
}
</style>