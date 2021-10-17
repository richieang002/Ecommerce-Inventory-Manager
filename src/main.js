import Vue from 'vue'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import PortalVue from 'portal-vue'
import VueRouter from "vue-router"
import vuetify from '@/plugins/vuetify' // path to vuetify export
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
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
import User from '@/components/User.vue'
import Summary from '@/components/Summary.vue'
import Product from '@/components/Product.vue'
import Overview from '@/components/Overview.vue'
import Import from '@/components/Import.vue'
import Products from '@/components/Products.vue'
import Platforms from '@/components/Platforms.vue'
import Connect from '@/components/Connect.vue'
import Export from '@/components/Export.vue'
import Psummary from '@/components/Psummary.vue'

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
    },
    {
      path: '/user',
      name: 'User',
      component: User,
      children: [
        { 
          path: "", 
          component: Overview,
          children: [
            { path: "summary", component: Summary },
          ]
        },
        { 
          path: "/import", 
          component: Import,
          children: [
            { path: "connect", component: Connect },
            { path: "export", component: Export },
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
       ]
    }
  ]
})

new Vue({
  vuetify,
  router,
  render: h => h(App),
}).$mount('#app')

export default router
