# Write your MySQL query statement below

WITH students_cross AS (
    SELECT
        st.student_id,
        st.student_name,
        su.subject_name
    FROM Students AS st
    CROSS JOIN Subjects AS su
)
, students_examinations AS (
    SELECT
        st.student_id,
        st.student_name,
        st.subject_name,
        ex.student_id AS exam_id
    FROM students_cross AS st
    LEFT JOIN Examinations AS ex
        ON st.student_id = ex.student_id
        AND st.subject_name = ex.subject_name
)

SELECT
    student_id,
    student_name,
    subject_name,
    COUNT(exam_id) AS attended_exams
FROM students_examinations
GROUP BY student_id, student_name, subject_name
ORDER BY student_id, subject_name
;
