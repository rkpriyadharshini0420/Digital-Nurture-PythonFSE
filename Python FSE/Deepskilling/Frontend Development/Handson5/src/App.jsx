import { useState, useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import StudentProfile from './components/StudentProfile';
import { initialCourses } from './data/data';

export default function App() {
  const [courses, setCourses] = useState(initialCourses);
  const [enrolled, setEnrolled] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [loading, setLoading] = useState(true);

  // Task 3: useEffect for lifecycle demonstration
  useEffect(() => {
    // Simulate API delay
    const timer = setTimeout(() => {
      setLoading(false);
    }, 1000);
    console.log("Courses initialized or updated");
    return () => clearTimeout(timer);
  }, [courses]); // Dependency array: Effect runs when 'courses' state changes

  const handleEnroll = (course) => {
    if (!enrolled.find(c => c.id === course.id)) {
      setEnrolled([...enrolled, course]);
    }
  };

  const filteredCourses = courses.filter(course => 
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  if (loading) return <div style={{ padding: '2rem' }}>Loading courses...</div>;

  return (
    <>
      <Header siteName="Student Portal" enrolledCount={enrolled.length} />
      
      <main style={{ padding: '20px' }}>
        <input 
          type="text" 
          placeholder="Search courses..." 
          onChange={(e) => setSearchTerm(e.target.value)}
          style={{ marginBottom: '20px', padding: '10px', width: '100%' }}
        />

        <div style={{ display: 'grid', gap: '20px', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))' }}>
          {filteredCourses.map(course => (
            <CourseCard 
              key={course.id} 
              course={course} 
              onEnroll={handleEnroll} 
            />
          ))}
        </div>

        <StudentProfile />
      </main>

      <Footer />
    </>
  );
}