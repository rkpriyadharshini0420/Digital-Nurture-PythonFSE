import apiClient from './apiClient';
export const getAllCourses = async () => {
  return await apiClient.get('/posts');
};
export const getCourseById = async (id) => {
  return await apiClient.get(`/posts/${id}`);
};
export const enrollStudent = async (studentId, courseId) => {
  return await apiClient.post('/enroll', { studentId, courseId });
};