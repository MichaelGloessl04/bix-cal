<template>
    <div>
        <h2>Rate Person</h2>
        <p>
            <span for="hot">Hot</span>
            <input id="hot" v-model="hot" type="range" min="1" max="10">
            <span>{{ hot }}</span>
        </p>
        <p>
            <span for="crazy">Crazy</span>
            <input id="crazy" v-model="crazy" type="range" min="1" max="10">
            <span>{{ crazy }}</span>
        </p>
        <p>
            <span for="nice">Nice</span>
            <input id="nice" v-model="nice" type="range" min="1" max="10">
            <span>{{ nice }}</span>
        </p>
        <p>
            <input id="comment" v-model="comment" type="message" placeholder="Comment" maxlength="20">
            <p id="comment-error">The Comment cant be longer than 20 letters.</p>
        </p>
        <button v-if="rated" @click="emits('changeRating')">Cancel</button>
        <button @click="submit">Submit</button>
    </div>
</template>

<script setup lang="ts">
import { addEntry } from '@/api/entry';
import type { EntryNoID } from '@/api/types/entry';
import { getUser } from '@/api/user';
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import { getAuth } from 'firebase/auth';

const route = useRoute()
const emits = defineEmits(['changeRating'])
defineProps(['rated'])

const hot = ref(5)
const crazy = ref(5)
const nice = ref(5)
const comment = ref('')

const submit = () => {
    console.log(hot.value, crazy.value, nice.value, comment.value)
    const currentUser = getAuth().currentUser
    if (!currentUser) {
        console.error('No user logged in')
        return
    }

    getUser(currentUser.email!)
        .then((user) => {
            const newEntry: EntryNoID = {
                person_id: Number(route.params.person_id),
                author_id: user.id,
                hot: hot.value,
                crazy: crazy.value,
                nice: nice.value,
                comment: comment.value
            }

            addEntry(newEntry)
                .then(() => {
                    console.log('Entry added')
                    emits('changeRating')
                })
                .catch((error) => {
                    console.error('Error adding entry:', error)
                })
        })
}
</script>