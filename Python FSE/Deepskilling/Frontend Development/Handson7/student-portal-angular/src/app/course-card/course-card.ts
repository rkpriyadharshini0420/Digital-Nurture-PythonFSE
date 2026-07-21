import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-course-card',
  standalone: true,
  templateUrl: './course-card.html',
})
export class CourseCardComponent {
  @Input() name: string = '';
  @Input() code: string = '';
  @Input() credits: number = 0;
  @Input() grade: string = '';
}