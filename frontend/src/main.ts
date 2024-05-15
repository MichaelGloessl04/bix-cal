import '@/assets/custom.scss'
import 'bootstrap'
import 'bootstrap-icons/font/bootstrap-icons.css'

import { createApp } from 'vue'
import { VueFire, VueFireAuth } from 'vuefire'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { firebaseApp } from '@/firebase'

const pinia = createPinia()
const app = createApp(App)

app.use(router)
app.use(pinia)
app.use(VueFire, {
    firebaseApp,
    modules: [
      VueFireAuth(),
    ],
  })

app.mount('#app')
