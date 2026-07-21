<script setup>
import { ref, computed, onMounted } from 'vue';
import CourseCard from '../components/CourseCard.vue';

const courses = ref([]);
const searchTerm = ref('');

onMounted(() => {
  courses.value = [
    { id: 1, name: 'Python Programming', code: 'CS101', credits: 3, grade: 'A' },
    { id: 2, name: 'Web Development', code: 'CS102', credits: 4, grade: 'B' },
    { id: 3, name: 'Machine Learning', code: 'CS103', credits: 3, grade: 'A' },
    { id: 4, name: 'IoT Fundamentals', code: 'CS104', credits: 2, grade: 'B' },
    { id: 5, name: 'Database Management', code: 'CS105', credits: 3, grade: 'A' }
  ];
});

const filteredCourses = computed(() => {
  return courses.value.filter(course => 
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  );
});
</script>

<template>
  <div class="courses-view">
    <h2>Available Courses</h2>
    
    <!-- Search Input -->
    <input 
      v-model="searchTerm" 
      placeholder="Search courses by name..." 
      class="search-bar"
    />
    
    <div class="course-list">
      <!-- Step 110: Render CourseCard for each course using props -->
      <CourseCard 
        v-for="course in filteredCourses" 
        :key="course.id"
        :id="course.id"
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
      />
    </div>
  </div>
</template>

<style scoped>
.courses-view {
  padding: 20px;
}

.search-bar {
  padding: 8px;
  width: 100%;
  max-width: 300px;
  margin-bottom: 20px;
  display: block;
}

.course-list {
  display: grid;
  gap: 15px;
}
</style>