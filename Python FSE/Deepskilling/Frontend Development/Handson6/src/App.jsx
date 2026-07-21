import { Routes, Route } from "react-router-dom";
import Header from "./Header";
import CoursesPage from "./CoursesPage"; // Ensure this matches your file name exactly

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<h1>Home Page</h1>} />
        <Route path="/courses" element={<CoursesPage />} />
        {/* Add other routes like /profile and /courses/:courseId later */}
      </Routes>
    </>
  );
}

export default App;