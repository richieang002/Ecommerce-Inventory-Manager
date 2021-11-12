import Vue from 'vue'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import PortalVue from 'portal-vue'
import VueRouter from "vue-router"
import vuetify from '@/plugins/vuetify' // path to vuetify export
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'

import '@/components/axios'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(faUserSecret)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(VueSidebarMenu)


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
import ForgetPassword from '@/components/ForgetPassword.vue'
import User from '@/components/User.vue'
import Summary from '@/components/Summary.vue'
import Product from '@/components/Product.vue'
import Import from '@/components/Import.vue'
import Products from '@/components/Products.vue'
import Platforms from '@/components/Platforms.vue'
import Connect from '@/components/Connect.vue'
import Export from '@/components/Export.vue'
import Psummary from '@/components/Psummary.vue'

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login,
      meta: {
        guest: true
      }
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
      meta: {
        guest: true
      }
    },
    {
      path: '/forget-password',
      name: 'ForgetPassword',
      component: ForgetPassword,
      meta: {
        guest: true
      }
    },
    {
      path: '/user',
      name: 'User',
      component: User,
      children: [
        { 
          path: "", 
          component: Import,
          children: [
            { path: "/import/connect", component: Connect },
            { path: "/import/export", component: Export },
          ]
        },
        { 
          path: "/products", 
          component: Products,
          children: [
            { path: "summary", component: Summary },
            { path: "product", component: Product },
          ]
        },
        { 
          path: "/platforms", 
          component: Platforms,
          children: [
            { path: "psummary", component: Psummary },
            { path: "product", component: Product },
          ]
        },
       ],
      meta: {
        requiresAuth: true
      }
    }
  ]
})

// Meta Handling
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem('token') == null) {
      next({
        path: '/',
        params: { nextUrl: to.fullPath }
      })
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.guest)) {
    if (localStorage.getItem('token') == null) {
      next()
    } else {
      next({ name: 'User' })
    }
  } else {
    next()
  }
})

new Vue({
  vuetify,
  router,
  render: h => h(App),
}).$mount('#app')

export default router
