## HANDS-ON 4

## Task 1: Baseline Performance — No Indexes


SELECT s.first_name, s.last_name, c.course_name
FROM enrollments e
JOIN students s ON s.student_id = e.student_id
JOIN courses c ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

## Task 2: Add Indexes and Compare Plans


CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

DROP TABLE IF EXISTS enrollments_clean;

CREATE TABLE enrollments_clean AS
SELECT 
    MIN(enrollment_id) AS enrollment_id,
    student_id,
    course_id,
    MAX(grade) AS grade
FROM enrollments
GROUP BY student_id, course_id;



CREATE INDEX idx_courses_course_code
ON courses(course_code);



SELECT s.first_name, s.last_name, c.course_name
FROM enrollments_clean e
JOIN students s ON s.student_id = e.student_id
JOIN courses c ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;



CREATE INDEX idx_enrollments_pending_grade
ON enrollments_clean(student_id);

## OUTPUT

<img width="1895" height="1062" alt="image" src="https://github.com/user-attachments/assets/bcd718d9-2e98-4ec6-9c2a-3a3272b805e6" />


##  Task 3: Identify and Fix the N+1 Problem

import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",   # change this
    database="your_database"    # change this
)

cursor = conn.cursor()


print("===== N+1 PROBLEM =====")

query_count = 0
start_time = time.time()

cursor.execute("SELECT enrollment_id, student_id, course_id FROM enrollments")
enrollments = cursor.fetchall()
query_count += 1

results = []

for e in enrollments:
    student_id = e[1]

    cursor.execute("""
        SELECT first_name, last_name
        FROM students
        WHERE student_id = %s
    """, (student_id,))

    results.append(cursor.fetchone())
    query_count += 1

end_time = time.time()

print("Total Queries Executed:", query_count)
print("Time Taken:", round(end_time - start_time, 4), "seconds")



print("\n===== OPTIMIZED JOIN =====")

query_count = 0
start_time = time.time()

cursor.execute("""
SELECT e.enrollment_id, s.first_name, s.last_name, c.course_name
FROM enrollments e
JOIN students s ON s.student_id = e.student_id
JOIN courses c ON c.course_id = e.course_id
""")

data = cursor.fetchall()
query_count += 1

end_time = time.time()

print("Total Queries Executed:", query_count)
print("Time Taken:", round(end_time - start_time, 4), "seconds")

conn.close()

## OUTPUT

<img width="1092" height="328" alt="image" src="https://github.com/user-attachments/assets/69bf952f-a4b6-4464-8c3b-37d0874dd5cc" />

