<template>
    <div class="table-box">
        <table class="table table-dark table-striped table-hover table-borderless rounded-pill">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Overall Score</th>
                    <th scope="col">Hot</th>
                    <th scope="col">Nice</th>
                    <th scope="col">Crazy</th>
                </tr>
            </thead>
            <tbody>
                <tr v-if="people.length > 0" v-for="person in people">
                    <PeopleListItem :person="person"/>
                </tr>
                <tr v-else>
                    <td class="col">No Results.</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import PeopleListItem from './PeopleListItem.vue';

import type { Person } from '@/types/person';

defineProps({
    people: {
        type: Array<Person>,
        required: true
    }
});
</script>

<style lang="scss">
$radius: 1rem;

.table {
    margin: 0 auto;
    width: 100%;
}

.table-box {
    padding: 0;
    margin: 0;
    width: 100%;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.61);
    border-radius: $radius;
}

tr:first-child td:first-child{
  border-top-left-radius: $radius;
}

tr:first-child td:last-child{
  border-top-right-radius: $radius;
}

tr:last-child td:first-child{
  border-bottom-left-radius: $radius;
}

tr:last-child td:last-child{
  border-bottom-right-radius: $radius;
}
</style>
