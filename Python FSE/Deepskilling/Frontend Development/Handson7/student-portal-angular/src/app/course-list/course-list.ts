import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './course-list.html',
  styleUrls: ['./course-list.css']
})
export class CourseListComponent {
  courses = [
    { name: 'Python Programming', credits: 4, grade: 'A' },
    { name: 'Java Development', credits: 3, grade: 'B+' },
    { name: 'Angular Framework', credits: 4, grade: 'A' },
    { name: 'Data Science', credits: 3, grade: 'A-' },
    { name: 'Cloud Computing', credits: 2, grade: 'B' }
  ];
}