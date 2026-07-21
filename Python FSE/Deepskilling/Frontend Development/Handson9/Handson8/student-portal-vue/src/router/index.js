import { createRouter, createWebHistory } from 'vue-router'
import CoursesView from '../views/CoursesView.vue'
import ProfileView from '../views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/courses', name: 'courses', component: CoursesView },
    { path: '/profile', name: 'profile', component: ProfileView },
  ]
})
router.beforeEach((to) => {
  console.log('Navigating to:', to.path)
})

export default router
