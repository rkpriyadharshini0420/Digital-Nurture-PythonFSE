import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchAllCourses, selectCourses, selectCoursesLoading } from './store/courseSlice';

function App() {
  const dispatch = useDispatch();
  const courses = useSelector(selectCourses);
  const loading = useSelector(selectCoursesLoading);
  // We use state to capture errors from our slice
  const error = useSelector((state) => state.courses.error); 

  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  if (loading) return <h2>Loading courses...</h2>;
  
  if (error) return <h2 style={{ color: 'red' }}>Error: {error}</h2>;

  return (
    <div>
      <h1>Digital Nurture - Course List</h1>
      <ul>
        {courses && courses.length > 0 ? (
          courses.map(course => <li key={course.id}>{course.title}</li>)
        ) : (
          <p>No courses available (or waiting for mock API).</p>
        )}
      </ul>
    </div>
  );
}

export default App;