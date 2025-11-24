
-- 7.1 Calculate the total cost to pay for a caregiver for all accepted appointments.

SELECT
    C.caregiver_user_id,
    U.given_name,
    U.surname,
    SUM(C.hourly_rate * A.work_hours) AS total_cost
FROM APPOINTMENT A
JOIN CAREGIVER C ON A.caregiver_user_id = C.caregiver_user_id
JOIN USER U ON C.caregiver_user_id = U.user_id
WHERE A.status = 'accepted'
GROUP BY C.caregiver_user_id, U.given_name, U.surname;
