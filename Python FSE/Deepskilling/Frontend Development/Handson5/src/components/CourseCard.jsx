export default function CourseCard({ course, onEnroll }) {
  return (
    <div style={{ border: '1px solid #ddd', padding: '1rem', borderRadius: '8px' }}>
      <h3>{course.name}</h3>
      <p>Code: {course.code} | Credits: {course.credits}</p>
      <button onClick={() => onEnroll(course)}>Enroll</button>
    </div>
  );
}