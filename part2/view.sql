-- 8.1 View all job applications and the applicants.


CREATE VIEW JobApplicationsView AS
SELECT
    JA.job_id,
    C.caregiver_user_id,
    U.given_name,
    U.surname,
    JA.date_applied
FROM JOB_APPLICATION JA
JOIN CAREGIVER C ON JA.caregiver_user_id = C.caregiver_user_id
JOIN USER U ON C.caregiver_user_id = U.user_id;

SELECT * FROM JobApplicationsView;
