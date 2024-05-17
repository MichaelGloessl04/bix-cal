import LoginView from '@/views/LoginView.vue'
import { getAuth } from 'firebase/auth'
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
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/person/:person_id',
      name: 'person',
      component: () => import('../views/PersonView.vue'),
      props: true
    },
    {
      path: '/people',
      name: 'people',
      component: () => import('../views/PeopleView.vue')
    },
    {
      path: '/add',
      name: 'add',
      component: () => import('../views/AddPersonView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('../views/NotFoundView.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (getAuth().currentUser) {
      next()
    } else {
      next('/login')
    }
  } else {
    next()
  }
})

export default router
