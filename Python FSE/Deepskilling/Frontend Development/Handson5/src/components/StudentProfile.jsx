import { useState } from 'react';

export default function StudentProfile() {
  const [profile, setProfile] = useState({ name: '', email: '', semester: '' });

  const handleChange = (e) => {
    setProfile({ ...profile, [e.target.name]: e.target.value });
  };

  return (
    <div style={{ marginTop: '2rem', padding: '1rem', border: '1px solid #ccc' }}>
      <h2>Student Profile</h2>
      <input name="name" placeholder="Name" onChange={handleChange} />
      <input name="email" placeholder="Email" onChange={handleChange} />
      <input name="semester" placeholder="Semester" onChange={handleChange} />
      <p>Preview: {profile.name} - {profile.email} - {profile.semester}</p>
    </div>
  );
}