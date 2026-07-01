## --HANDS-ON 3--
--Priyadharshini R K--

## --Task 1--
--Subqueries--
```
SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) avg_table
);


SELECT
    c.course_id,
    c.course_name
FROM courses c
WHERE NOT EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
      AND e.grade <> 'A'
);


SELECT
    p.professor_id,
    p.prof_name,
    p.department_id,
    p.salary
FROM professors p
WHERE p.salary =
(
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);



SELECT *
FROM
(
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM professors
    GROUP BY department_id
) AS dept_avg
WHERE avg_salary > 85000;

```

## --Task 2--
--Views--
```

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS full_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,
    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                ELSE 0
            END
        ),2
    ) AS GPA
FROM students s
JOIN departments d
ON s.department_id = d.department_id
LEFT JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY
s.student_id,
s.first_name,
s.last_name,
d.dept_name;


CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.student_id) AS total_enrollments,
    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                ELSE 0
            END
        ),2
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY
c.course_id,
c.course_name,
c.course_code;


SELECT *
FROM vw_student_enrollment_summary
WHERE GPA > 3.0;


UPDATE vw_student_enrollment_summary
SET GPA = 4
WHERE student_id = 1;


DROP VIEW IF EXISTS vw_course_stats;
DROP VIEW IF EXISTS vw_student_enrollment_summary;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    student_id,
    first_name,
    last_name,
    department_id
FROM students
WHERE department_id IS NOT NULL
WITH CHECK OPTION;
```

## --Task 3--
--Stored Procedures & Transactions--
``
DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN
    IF EXISTS (
        SELECT 1
        FROM enrollments
        WHERE student_id = p_student_id
          AND course_id = p_course_id
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Student is already enrolled in this course';
    ELSE
        INSERT INTO enrollments(student_id, course_id, enrollment_date)
        VALUES (p_student_id, p_course_id, p_enrollment_date);
    END IF;
END $$

DELIMITER ;

CALL sp_enroll_student(1,4,CURDATE());

CREATE TABLE department_transfer_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    old_department INT,
    new_department INT,
    transfer_date DATETIME,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (old_department) REFERENCES departments(department_id),
    FOREIGN KEY (new_department) REFERENCES departments(department_id)
);

DELIMITER $$

CREATE PROCEDURE sp_transfer_student(
    IN p_student_id INT,
    IN p_new_department INT
)
BEGIN
    DECLARE v_old_department INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
    END;

    START TRANSACTION;

    SELECT department_id
    INTO v_old_department
    FROM students
    WHERE student_id = p_student_id;

    UPDATE students
    SET department_id = p_new_department
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log
    (student_id, old_department, new_department, transfer_date)
    VALUES
    (p_student_id, v_old_department, p_new_department, NOW());

    COMMIT;
END $$

DELIMITER ;



CALL sp_transfer_student(1,999);

SELECT *
FROM students
WHERE student_id = 1;

SELECT *
FROM department_transfer_log;


START TRANSACTION;

INSERT INTO enrollments(student_id, course_id, enrollment_date)
VALUES (2,3,CURDATE());

SAVEPOINT sp1;

INSERT INTO enrollments(student_id, course_id, enrollment_date)
VALUES (2,999,CURDATE());

ROLLBACK TO sp1;

COMMIT;

SELECT *
FROM enrollments
WHERE student_id = 2;



## OUTPUT:

<img width="1918" height="1078" alt="Screenshot 2026-07-01 103807" src="https://github.com/user-attachments/assets/20a0d65e-a4f8-492a-ae69-6a50f665610a" />







