import { courses } from './data.js';

const grid = document.querySelector('.course-grid');
const searchInput = document.querySelector('#searchInput');
const sortBtn = document.querySelector('#sortBtn');
const totalDisplay = document.querySelector('#totalCreditsDisplay');

function render(data) {
    grid.innerHTML = '';
    let total = 0;
    data.forEach(course => {
        total += course.credits;
        const article = document.createElement('article');
        article.className = 'course-card';
        article.innerHTML = `<h3>${course.name}</h3><p>${course.code}</p><span>${course.credits} cr</span>`;
        grid.appendChild(article);
    });
    totalDisplay.textContent = `Total Credits: ${total}`;
}

grid.addEventListener('click', (e) => {
    const card = e.target.closest('.course-card');
    if (card) alert('Course clicked!');
});

searchInput.addEventListener('input', (e) => {
    const filtered = courses.filter(c => c.name.toLowerCase().includes(e.target.value.toLowerCase()));
    render(filtered);
});

sortBtn.addEventListener('click', () => {
    const sorted = [...courses].sort((a, b) => b.credits - a.credits);
    render(sorted);
});

render(courses);