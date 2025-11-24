-- 5.1 Select caregiver and member names for the accepted appointments.

SELECT
    c_user.given_name AS caregiver_given,
    c_user.surname AS caregiver_surname,
    m_user.given_name AS member_given,
    m_user.surname AS member_surname
FROM APPOINTMENT A
JOIN CAREGIVER C ON A.caregiver_user_id = C.caregiver_user_id
JOIN USER c_user ON C.caregiver_user_id = c_user.user_id
JOIN MEMBER M ON A.member_user_id = M.member_user_id
JOIN USER m_user ON M.member_user_id = m_user.user_id
WHERE A.status = 'accepted';

-- 5.2 List job ids that contain ‘soft-spoken’ in their other requirements.
SELECT job_id
FROM JOB
WHERE other_requirements LIKE '%soft-spoken%';


-- 5.3 List the work hours of all babysitter positions.
SELECT A.work_hours
FROM APPOINTMENT A
JOIN CAREGIVER C ON A.caregiver_user_id = C.caregiver_user_id
WHERE C.caregiving_type = 'babysitter';


-- 5.4 List the members who are looking for Elderly Care in Astana and have “No pets.” rule.
SELECT U.given_name, U.surname
FROM MEMBER M
JOIN USER U ON M.member_user_id = U.user_id
JOIN JOB J ON M.member_user_id = J.member_user_id
WHERE J.required_caregiving_type = 'caregiver for elderly'
  AND U.city = 'Astana'
  AND M.house_rules LIKE '%No pets.%';
