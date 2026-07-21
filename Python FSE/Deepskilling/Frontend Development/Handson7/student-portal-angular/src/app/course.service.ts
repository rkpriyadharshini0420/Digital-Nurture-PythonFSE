import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CourseService {
  private http = inject(HttpClient);

  getCourses() {
    return this.http.get('https://jsonplaceholder.typicode.com/posts?_limit=5');
  }
}