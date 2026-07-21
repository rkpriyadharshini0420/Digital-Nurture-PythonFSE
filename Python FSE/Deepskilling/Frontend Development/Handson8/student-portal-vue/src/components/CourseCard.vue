<script setup>
import { useEnrollmentStore } from '../stores/enrollment';

const props = defineProps({ 
  id: Number,
  name: String, 
  code: String, 
  credits: Number, 
  grade: String 
});

const store = useEnrollmentStore();

const handleEnroll = () => {
  
  store.enroll({
    id: props.id,
    name: props.name,
    code: props.code,
    credits: props.credits,
    grade: props.grade
  });
};
</script>

<template>
  <div class="course-card">
    <h3>{{ name }} ({{ code }})</h3>
    <p>Credits: {{ credits }} | Grade: {{ grade }}</p>
    
    <!-- Button triggers the Pinia action -->
    <button @click="handleEnroll">Enroll</button>
  </div>
</template>

<style scoped>
.course-card {
  border: 1px solid #ddd;
  padding: 15px;
  margin: 10px 0;
  border-radius: 8px;
  background-color: #fff;
}

button {
  cursor: pointer;
  padding: 5px 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
}
</style>