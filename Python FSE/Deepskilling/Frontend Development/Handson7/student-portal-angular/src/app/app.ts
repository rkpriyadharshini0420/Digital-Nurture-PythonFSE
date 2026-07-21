import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common'; // Required for *ngFor

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule], 
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('Student Portal');
  
  courses = [
    { name: 'Python Programming', credits: 4, grade: 'A' },
    { name: 'Java Development', credits: 3, grade: 'B+' },
    { name: 'Angular Framework', credits: 4, grade: 'A' },
    { name: 'Data Science', credits: 3, grade: 'A-' },
    { name: 'Cloud Computing', credits: 2, grade: 'B' }
  ];
}