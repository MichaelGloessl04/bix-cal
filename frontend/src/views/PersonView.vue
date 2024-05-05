<template>
    <PersonPage :person_id="route.params.person_id" />
</template>

<script setup lang="ts">
import PersonPage from '@/components/PersonPage.vue';

import { useRoute } from 'vue-router';

const route = useRoute();
</script>