import { useDispatch } from 'react-redux';
import { enroll } from './enrollmentSlice';

export default function CoursesPage() {
  const dispatch = useDispatch();

  // Define a simple list of courses
  const courses = [
    { id: 1, name: 'React' },
    { id: 2, name: 'Python' },
    { id: 3, name: 'Machine Learning' }
  ];

  return (
    <div>
      <h1>Courses</h1>
      <ul>
        {courses.map((course) => (
          <li key={course.id}>
            {course.name} 
            <button onClick={() => dispatch(enroll(course))}>Enroll</button>
          </li>
        ))}
      </ul>
    </div>
  );
}