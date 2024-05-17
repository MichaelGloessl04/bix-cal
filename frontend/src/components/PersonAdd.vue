<template>
    <div @submit.prevent="submit">
        <form>
            <div>
                <label for="name">Name</label>
                <input type="text" v-model="person.name" id="name" placeholder="Name" required/>
            </div>
            <div>
                <label for="surname">Surname</label>
                <input type="text" v-model="person.surname" id="surname" placeholder="Surname" required/>
            </div>
            <button type="submit">Add</button>
        </form>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import { addPerson } from '@/api/person'

import type { Ref } from 'vue'
import type { PersonNoID } from '@/api/types/person'

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
