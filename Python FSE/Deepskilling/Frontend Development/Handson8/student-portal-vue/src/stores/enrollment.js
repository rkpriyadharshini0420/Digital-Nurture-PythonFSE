import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useEnrollmentStore = defineStore('enrollment', () => {
  const enrolledCourses = ref([])
  const totalCredits = computed(() => 
    enrolledCourses.value.reduce((acc, course) => acc + course.credits, 0)
  )
  
  function enroll(course) {
    enrolledCourses.value.push(course)
  }
  
  return { enrolledCourses, totalCredits, enroll }
})
