import { createContext, useState } from 'react';

export const EnrollmentContext = createContext();

export const EnrollmentProvider = ({ children }) => {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const enroll = (course) => {
    setEnrolledCourses([...enrolledCourses, course]);
  };

  return (
    <EnrollmentContext.Provider value={{ enrolledCourses, enroll }}>
      {children}
    </EnrollmentContext.Provider>
  );
};