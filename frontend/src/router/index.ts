import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/person/:person_id',
      name: 'person',
      component: () => import('../views/PersonView.vue'),
      props: true
    },
    {
      path: '/add',
      name: 'add',
      component: () => import('../views/AddPersonView.vue')
    }
  ]
})

export default router
