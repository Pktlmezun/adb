-- 4.1	Delete the jobs posted by Amina Aminova.
SELECT * FROM JOB
WHERE member_user_id IN (
    SELECT member_user_id
    FROM MEMBER
    WHERE member_user_id IN (
        SELECT user_id
        FROM USER
        WHERE given_name = 'Amina'
          AND surname = 'Aminova'
    )
);

DELETE FROM JOB
WHERE member_user_id IN (
    SELECT member_user_id
    FROM MEMBER
    WHERE member_user_id IN (
        SELECT user_id
        FROM USER
        WHERE given_name = 'Amina'
          AND surname = 'Aminova'
    )
);

SELECT * FROM JOB
WHERE member_user_id IN (
    SELECT member_user_id
    FROM MEMBER
    WHERE member_user_id IN (
        SELECT user_id
        FROM USER
        WHERE given_name = 'Amina'
          AND surname = 'Aminova'
    )
);




-- 4.2	Delete all members who live on Kabanbay Batyr street.
--
SELECT * FROM MEMBER
WHERE member_user_id IN (
    SELECT member_user_id
    FROM ADDRESS
    WHERE street = 'Kabanbay Batyr'
);

DELETE FROM MEMBER
WHERE member_user_id IN (
    SELECT member_user_id
    FROM ADDRESS
    WHERE street = 'Kabanbay Batyr'
);


SELECT * FROM MEMBER
WHERE member_user_id IN (
    SELECT member_user_id
    FROM ADDRESS
    WHERE street = 'Kabanbay Batyr'
);
