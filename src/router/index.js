import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Solutions from '../views/Solutions.vue'
import Products from '../views/Products.vue'
import Cases from '../views/Cases.vue'
import Community from '../views/Community.vue'
import Support from '../views/Support.vue'
import Login from '../views/Login.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/solutions', component: Solutions },
  { path: '/products', component: Products },
  { path: '/cases', component: Cases },
  { path: '/community', component: Community },
  { path: '/support', component: Support },
  { path: '/login', component: Login }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return new Promise((resolve) => {
      setTimeout(() => {
        if (to.hash) {
          resolve({ el: to.hash, behavior: 'smooth' })
        } else if (savedPosition) {
          resolve(savedPosition)
        } else {
          resolve({ top: 0 })
        }
      }, 100)
    })
  }
})

export default router
