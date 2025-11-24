-- 6.1 Count the number of applicants for each job posted by a member (multiple joins with aggregation)
SELECT
    J.job_id,
    COUNT(JA.caregiver_user_id) AS applicant_count
FROM JOB J
LEFT JOIN JOB_APPLICATION JA ON J.job_id = JA.job_id
GROUP BY J.job_id;


-- 6.2 Total hours spent by care givers for all accepted appointments (multiple joins with aggregation)
SELECT
    C.caregiver_user_id,
    U.given_name,
    U.surname,
    SUM(A.work_hours) AS total_hours
FROM APPOINTMENT A
JOIN CAREGIVER C ON A.caregiver_user_id = C.caregiver_user_id
JOIN USER U ON C.caregiver_user_id = U.user_id
WHERE A.status = 'accepted'
GROUP BY C.caregiver_user_id, U.given_name, U.surname;

-- 6.3 Average pay of caregivers based on accepted appointments (join with aggregation)
SELECT
    C.caregiver_user_id,
    U.given_name,
    U.surname,
    ROUND(AVG(C.hourly_rate * A.work_hours), 2) AS avg_pay
FROM APPOINTMENT A
JOIN CAREGIVER C ON A.caregiver_user_id = C.caregiver_user_id
JOIN USER U ON C.caregiver_user_id = U.user_id
WHERE A.status = 'accepted'
GROUP BY C.caregiver_user_id, U.given_name, U.surname;

-- 6.4 Caregivers who earn above average based on accepted appointments (multiple join with aggregation and nested query)

SELECT
    C.caregiver_user_id,
    U.given_name,
    U.surname,
    SUM(A.work_hours * C.hourly_rate) AS total_earnings
FROM APPOINTMENT A
JOIN CAREGIVER C ON A.caregiver_user_id = C.caregiver_user_id
JOIN USER U ON C.caregiver_user_id = U.user_id
WHERE A.status = 'accepted'
GROUP BY C.caregiver_user_id, U.given_name, U.surname
HAVING SUM(A.work_hours * C.hourly_rate) >
(
    SELECT AVG(sub.total_earnings)
    FROM (
        SELECT
            C2.caregiver_user_id,
            SUM(A2.work_hours * C2.hourly_rate) AS total_earnings
        FROM APPOINTMENT A2
        JOIN CAREGIVER C2 ON A2.caregiver_user_id = C2.caregiver_user_id
        WHERE A2.status = 'accepted'
        GROUP BY C2.caregiver_user_id
    ) AS sub
);
