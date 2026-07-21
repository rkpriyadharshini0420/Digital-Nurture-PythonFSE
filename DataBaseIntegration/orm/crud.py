# =========================================================================
# HANDS-ON 6: ORM CRUD OPERATIONS & PERFORMANCE TESTING
# Participant:Priyadharshini R K
# =========================================================================
"""
BENCHMARK LOG ANALYSIS (Task 3):
- Under standard Lazy Loading, retrieving all enrollments and fetching their associated 
  student/course data loops separate queries sequentially, generating N+1 execution loops (13 queries total).
- Utilizing SQLAlchemy's eager `joinedload` strategy optimization issues 1 unified SQL standard JOIN operation,
  reducing database round-trips from 13 down to 1 query seamlessly.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from datetime import date
from models import Base, Department, Student, Course, Enrollment

# Database driver configuration
DATABASE_URL = "sqlite:///./college_db_orm.db"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True prints all SQL queries generated

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def execute_crud_operations():
    # Auto-generate schema tables cleanly
    Base.metadata.create_all(engine)
    
    # Clean database clear down to avoid duplication conflicts on run resets
    session.query(Enrollment).delete()
    session.query(Student).delete()
    session.query(Course).delete()
    session.query(Department).delete()
    session.commit()

    # Step 1: INSERT 3 Departments & 5 Students
    cs_dept = Department(dept_name="Computer Science", head_of_dept="Dr. Ramesh Kumar", budget=850000.00)
    ec_dept = Department(dept_name="Electronics", head_of_dept="Dr. Priya Nair", budget=620000.00)
    me_dept = Department(dept_name="Mechanical", head_of_dept="Dr. Suresh Iyer", budget=540000.00)
    session.add_all([cs_dept, ec_dept, me_dept])
    session.commit()

    s1 = Student(first_name="Arjun", last_name="Mehta", email="arjun@college.edu", date_of_birth=date(2003,4,12), department_id=cs_dept.department_id, enrollment_year=2022)
    s2 = Student(first_name="Priya", last_name="Suresh", email="priya@college.edu", date_of_birth=date(2003,7,25), department_id=cs_dept.department_id, enrollment_year=2022)
    s3 = Student(first_name="Rohan", last_name="Verma", email="rohan@college.edu", date_of_birth=date(2002,11,8), department_id=ec_dept.department_id, enrollment_year=2021)
    s4 = Student(first_name="Maleni", last_name="M", email="maleni.m@college.edu", date_of_birth=date(2004,5,20), department_id=cs_dept.department_id, enrollment_year=2022)
    s5 = Student(first_name="Rahul", last_name="Sharma", email="rahul@college.edu", date_of_birth=date(2003,12,11), department_id=me_dept.department_id, enrollment_year=2023)
    session.add_all([s1, s2, s3, s4, s5])
    session.commit()

    # Step 2: INSERT 3 Courses & 4 Enrollments
    c1 = Course(course_name="Data Structures", course_code="CS101", credits=4, department_id=cs_dept.department_id)
    c2 = Course(course_name="Database Systems", course_code="CS102", credits=3, department_id=cs_dept.department_id)
    c3 = Course(course_name="Circuit Theory", course_code="EC101", credits=3, department_id=ec_dept.department_id)
    session.add_all([c1, c2, c3])
    session.commit()

    e1 = Enrollment(student_id=s1.student_id, course_id=c1.course_id, enrollment_date=date(2022,7,1), grade="A")
    e2 = Enrollment(student_id=s2.student_id, course_id=c1.course_id, enrollment_date=date(2022,7,1), grade="B")
    e3 = Enrollment(student_id=s4.student_id, course_id=c2.course_id, enrollment_date=date(2022,7,1), grade="A")
    e4 = Enrollment(student_id=s3.student_id, course_id=c3.course_id, enrollment_date=date(2021,7,1), grade="A")
    session.add_all([e1, e2, e3, e4])
    session.commit()

    # Step 3: READ - Filter students by Computer Science department
    print("\n--- [READ TASK] Computer Science Students ---")
    cs_students = session.query(Student).join(Department).filter(Department.dept_name == "Computer Science").all()
    for student in cs_students:
        print(f"Student: {student.first_name} {student.last_name} ({student.email})")

    # Step 4: READ OPTIMIZED - Fetch enrollments with eager loading (Fixing N+1)
    print("\n--- [OPTIMIZED READ TASK] Eager Load Joined Query ---")
    enrollments = session.query(Enrollment).options(joinedload(Enrollment.student), joinedload(Enrollment.course)).all()
    for enrollment in enrollments:
        print(f"Enrollment: {enrollment.student.first_name} -> Course: {enrollment.course.course_name} (Grade: {enrollment.grade})")

    # Step 5: UPDATE - Update enrollment year by specific student email
    print("\n--- [UPDATE TASK] Altering Student Milestone Data ---")
    target_student = session.query(Student).filter(Student.email == "maleni.m@college.edu").first()
    if target_student:
        target_student.enrollment_year = 2023
        session.commit()
        print(f"Updated {target_student.first_name}'s enrollment year to {target_student.enrollment_year}")

    # Step 6: DELETE - Remove an enrollment record instance
    print("\n--- [DELETE TASK] Removing Target Record ---")
    delete_target = session.query(Enrollment).filter(Enrollment.grade == "B").first()
    if delete_target:
        session.delete(delete_target)
        session.commit()
        print("Successfully removed enrollment record.")

if __name__ == "__main__":
    execute_crud_operations()
