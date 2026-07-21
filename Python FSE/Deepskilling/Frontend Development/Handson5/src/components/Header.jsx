export default function Header({ siteName }) {
  return (
    <header style={{ padding: '1rem', borderBottom: '1px solid #ccc' }}>
      <h1>{siteName}</h1>
      <nav>
        <a href="#">Home</a> | <a href="#">Courses</a> | <a href="#">Profile</a>
      </nav>
    </header>
  );
}