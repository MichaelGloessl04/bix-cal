import '@/assets/custom.scss'
import 'bootstrap'
import 'bootstrap-icons/font/bootstrap-icons.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { initializeApp } from 'firebase/app'
import { getAnalytics } from 'firebase/analytics'

const app = createApp(App)

const firebaseConfig = {
  apiKey: 'AIzaSyBlPMQ0310tRLudTxw2lyN5agBCIvo_sHw',
  authDomain: 'bixcal-9a93c.firebaseapp.com',
  projectId: 'bixcal-9a93c',
  storageBucket: 'bixcal-9a93c.appspot.com',
  messagingSenderId: '75319400869',
  appId: '1:75319400869:web:c0b8cdac2ffb64f456f04c'
}

const fireApp = initializeApp(firebaseConfig)
getAnalytics(fireApp)

app.use(router)

app.mount('#app')
