import Vue from 'vue'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import PortalVue from 'portal-vue'
import VueRouter from "vue-router"
import vuetify from '@/plugins/vuetify' // path to vuetify export

Vue.use(VueRouter)
Vue.use(PortalVue)

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.config.productionTip = false

import Login from '@/components/Login.vue'
import Register from '@/components/Register.vue'

const router = new VueRouter({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    }
  ]
})

new Vue({
  vuetify,
  router,
  render: h => h(App),
}).$mount('#app')

export default router
