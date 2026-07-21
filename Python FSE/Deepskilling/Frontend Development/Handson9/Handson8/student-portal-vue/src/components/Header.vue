<script setup>
import { RouterLink } from 'vue-router';
import { useEnrollmentStore } from '../stores/enrollment';

// Access the Pinia store to display the count
const store = useEnrollmentStore();
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/courses">Courses</RouterLink>
      <RouterLink to="/profile">Profile</RouterLink>
      
      <!-- Display enrolled course count -->
      <div class="enrollment-badge">
        Enrolled: {{ store.enrolledCourses.length }}
      </div>
    </nav>
  </header>
</template>

<style scoped>
header {
  padding: 1rem;
  background-color: #f8f9fa;
  border-bottom: 1px solid #ddd;
}
nav {
  display: flex;
  gap: 20px;
  align-items: center;
}
.enrollment-badge {
  margin-left: auto;
  font-weight: bold;
  color: #2c3e50;
}
</style>