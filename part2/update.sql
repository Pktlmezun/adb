-- 3.1 Update the phone number of Arman Armanov to +77773414141.
--
SELECT * FROM user WHERE given_name = 'Arman' AND surname = 'Armanov';

UPDATE user
SET phone_number = '+77773414141'
WHERE given_name = 'Arman' AND surname = 'Armanov';

SELECT * FROM user WHERE given_name = 'Arman' AND surname = 'Armanov';



-- 3.2 Add $0.3 commission fee to the Caregivers’ hourly rate if it's less than $10, or 10% if it's not.
--
SELECT hourly_rate from caregiver;

UPDATE caregiver
SET hourly_rate =
    CASE
        WHEN hourly_rate < 10
            THEN hourly_rate + 0.3
        ELSE hourly_rate * 1.10
    END;

SELECT hourly_rate from caregiver;
