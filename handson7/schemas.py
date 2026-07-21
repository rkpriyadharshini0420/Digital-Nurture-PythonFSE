from pydantic import BaseModel, EmailStr
from typing import List, Optional

class CourseBase(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    class Config:
        from_attributes = True

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int