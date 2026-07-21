import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

export default function Header() {
  // Select only the data we need from the Redux state
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);

  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/courses">Courses</Link>
      
      {/* Access the length of the array from the Redux store */}
      <span> | Enrolled: {enrolledCourses.length}</span>
    </nav>
  );
}