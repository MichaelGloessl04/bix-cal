<template>
    <div>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Overall Score</th>
                    <th>Hot</th>
                    <th>Nice</th>
                    <th>Crazy</th>
                </tr>
            </thead>
            <tbody>
                <tr v-if="people.length > 0" v-for="person in people">
                    <PeopleListItem :person="person"/>
                </tr>
                <tr v-else>
                    <td>No Results.</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import PeopleListItem from './PeopleListItem.vue';

import type { Person } from '@/api/types/person';

defineProps({
    people: {
        type: Array<Person>,
        required: true
    }
});
</script>
