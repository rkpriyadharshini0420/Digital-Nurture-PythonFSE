from fastapi import FastAPI, Depends, status, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from contextlib import asynccontextmanager
from database import get_db, engine
from models import Base, Course, Student, Enrollment
from schemas import CourseCreate, CourseResponse, EnrollmentCreate

# 1. Lifespan context manager for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown: Clean up connection pool
    await engine.dispose()

# 2. Define FastAPI app with lifespan
app = FastAPI(
    title="Course Management API",
    description="API for managing courses, students, and enrollments.",
    version="1.0.0",
    contact={"name": "Developer", "email": "dev@example.com"},
    lifespan=lifespan
)

# Background Task function
def send_confirmation_email(student_email: str):
    print(f'Sending confirmation to {student_email}')

# --- Courses Endpoints ---

@app.post("/api/courses/", status_code=status.HTTP_201_CREATED, tags=['Courses'], response_model=CourseResponse)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    new_course = Course(**course.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course

@app.delete("/api/courses/{id}", tags=['Courses'], status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == id))
    course = result.scalar_one_or_none()
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    await db.delete(course)
    await db.commit()
    return None

# --- Enrollment Endpoints ---

@app.post("/api/enrollments/", status_code=status.HTTP_201_CREATED, tags=['Enrollments'])
async def create_enrollment(enroll: EnrollmentCreate, background_tasks: BackgroundTasks):
    # Trigger background task
    background_tasks.add_task(send_confirmation_email, "student@example.com")
    return {"message": "Enrollment successful"}

@app.get('/')
async def root():
    return {'message': 'API running'}