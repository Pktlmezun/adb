INSERT INTO USER (email, given_name, surname, city, phone_number, profile_description, password) VALUES
-- Caregivers (user_id 1-10)
('aigerim.nur@gmail.com', 'Aigerim', 'Nurbekkyzy', 'Astana', '+77771234567', '5 years of experience as a babysitter. I love working with children.', 'pass123'),
('daulet.serik@gmail.com', 'Daulet', 'Serikuly', 'Almaty', '+77771234568', 'Certified elderly caregiver. Calm and responsible professional.', 'pass123'),
('alua.samat@gmail.com', 'Alua', 'Samatkyzy', 'Astana', '+77771234569', 'Active playmate for children. Background in child psychology.', 'pass123'),
('eldar.askar@gmail.com', 'Eldar', 'Askaruly', 'Shymkent', '+77771234570', 'Professional babysitter with first aid certification.', 'pass123'),
('zhanel.kaisar@gmail.com', 'Zhanel', 'Kaisarkyzy', 'Astana', '+77771234571', 'Experienced in elderly care with medical background.', 'pass123'),
('marat.talgat@gmail.com', 'Marat', 'Talgatuly', 'Almaty', '+77771234572', 'Creative children’s play organizer. Background as an art teacher.', 'pass123'),
('asyl.naz@gmail.com', 'Asyl', 'Nazymskyzy', 'Astana', '+77771234573', 'Specialized in caring for infants and newborns.', 'pass123'),
('nurik.kairat@gmail.com', 'Nurik', 'Kairatuly', 'Karaganda', '+77771234574', 'Medically trained caregiver for the elderly.', 'pass123'),
('saule.bek@gmail.com', 'Saule', 'Bekkyzy', 'Astana', '+77771234575', 'Playmate and academic assistant for school-age children.', 'pass123'),
('ramazan.erlan@gmail.com', 'Ramazan', 'Erlanuly', 'Almaty', '+77771234576', 'Reliable babysitter with excellent references.', 'pass123'),
('arman.armanov@gmail.com', 'Arman', 'Armanov', 'Astana', '+77771234577', 'Experienced babysitter with CPR certification.', 'pass123'),

-- Members (user_id 11-22)
('akmaral.ak@gmail.com', 'Akmaral', 'Akynkyzy', 'Astana', '+77772345678', 'Mother of two looking for a reliable babysitter.', 'pass456'),
('serik.bolat@gmail.com', 'Serik', 'Bolatuly', 'Almaty', '+77772345679', 'Looking for a caregiver for my elderly father.', 'pass456'),
('gulmira.t@gmail.com', 'Gulmira', 'Toleukhanakyzy', 'Astana', '+77772345680', 'Working mother needing after-school care.', 'pass456'),
('daniyar.oral@gmail.com', 'Daniyar', 'Oraluly', 'Shymkent', '+77772345681', 'Need a babysitter for weekends.', 'pass456'),
('aida.kairat@gmail.com', 'Aida', 'Kairatkzy', 'Astana', '+77772345682', 'Looking for a caregiver for my grandmother.', 'pass456'),
('yerlan.nur@gmail.com', 'Yerlan', 'Nurlanuly', 'Almaty', '+77772345683', 'Single father looking for a reliable babysitter.', 'pass456'),
('diana.zhan@gmail.com', 'Diana', 'Zhanatkyzy', 'Astana', '+77772345684', 'Need a playmate for my 7-year-old daughter.', 'pass456'),
('bolat.sarsen@gmail.com', 'Bolat', 'Sarsenuly', 'Karaganda', '+77772345685', 'Need a caregiver for my mother with dementia.', 'pass456'),
('aliya.muk@gmail.com', 'Aliya', 'Mubarakkyzy', 'Astana', '+77772345686', 'Looking for a part-time babysitter.', 'pass456'),
('timur.sadan@gmail.com', 'Timur', 'Sadanuly', 'Almaty', '+77772345687', 'Need post-surgery care for my father.', 'pass456'),
('amina.aminova@gmail.com', 'Amina', 'Aminova', 'Astana', '+77772345688', 'Looking for reliable caregivers for my family.', 'pass456');


-- Insert CAREGIVER records (11 caregivers)
INSERT INTO CAREGIVER (caregiver_user_id, photo, gender, caregiving_type, hourly_rate) VALUES
(1, 'aigerim_photo.jpg', 'Female', 'babysitter', 8.50),
(2, 'daulet_photo.jpg', 'Male', 'caregiver for elderly', 12.00),
(3, 'alua_photo.jpg', 'Female', 'playmate for children', 9.00),
(4, 'eldar_photo.jpg', 'Male', 'babysitter', 9.50),
(5, 'zhanel_photo.jpg', 'Female', 'caregiver for elderly', 11.50),
(6, 'marat_photo.jpg', 'Male', 'playmate for children', 8.00),
(7, 'asyl_photo.jpg', 'Female', 'babysitter', 7.50),
(8, 'nurik_photo.jpg', 'Male', 'caregiver for elderly', 13.00),
(9, 'saule_photo.jpg', 'Female', 'playmate for children', 9.50),
(10, 'ramazan_photo.jpg', 'Male', 'babysitter', 8.00),
(11, 'arman_photo.jpg', 'Male', 'babysitter', 10.50);


INSERT INTO MEMBER (member_user_id, house_rules, dependent_description) VALUES
(12, 'No smoking. No pets. Basic hygiene must be maintained.', 'I have two children, ages 3 and 5. Both are very active and enjoy outdoor play.'),
(13, 'The house should stay quiet. Loud noises are undesirable.', 'My father is 78 years old with limited mobility. He needs daily care.'),
(14, 'Punctuality is mandatory. Phone use is not allowed during working hours.', 'My 8-year-old daughter needs after-school supervision and homework assistance.'),
(15, 'The caregiver must be comfortable with pets. We have a dog.', 'My 4-year-old son needs weekend supervision.'),
(16, 'No pets. Experience with dementia is required.', 'My 82-year-old grandmother has mild dementia and needs ongoing monitoring.'),
(17, 'Rules are flexible. Responsibility is the main requirement.', 'My 6-year-old son enjoys playing football.'),
(18, 'Creative activities are encouraged. Screen time is limited.', 'My 7-year-old daughter loves drawing and art activities.'),
(19, 'Medical knowledge is required. Safety instructions will be provided.', 'My mother has Alzheimer''s and requires specialized care.'),
(20, 'No allergy concerns. Meals will be provided.', 'My 2-year-old twins need care during working hours.'),
(21, 'Experience working with elderly individuals is essential.', 'My father is recovering from surgery and needs mobility assistance.'),
(22, 'No pets. Cleanliness is very important.', 'Looking for multiple caregivers for different family members.');


INSERT INTO ADDRESS (member_user_id, house_number, street, town) VALUES
(12, '45', 'Kabanbay Batyr', 'Astana'),
(13, '23', 'Respublika Avenue', 'Almaty'),
(14, '12', 'Turan Street', 'Astana'),
(15, '89', 'Tauke Khan Avenue', 'Shymkent'),
(16, '34', 'Dostyk Avenue', 'Astana'),
(17, '56', 'Abay Street', 'Almaty'),
(18, '78', 'Kabanbay Batyr', 'Astana'),
(19, '91', 'Nazarbayev Avenue', 'Karaganda'),
(20, '15', 'Mangilik El Avenue', 'Astana'),
(21, '67', 'Satpaev Street', 'Almaty'),
(22, '99', 'Syganak Street', 'Astana');

INSERT INTO JOB (member_user_id, required_caregiving_type, other_requirements, date_posted) VALUES
(12, 'babysitter', 'Must be soft-spoken and patient with young children. Experience with toddlers required.', '2025-11-01'),
(12, 'playmate for children', 'Energetic person needed for outdoor activities. Must be available on weekends.', '2025-11-03'),
(13, 'caregiver for elderly', 'Need someone with medical background. Weekday mornings 9AM-12PM.', '2025-11-02'),
(14, 'babysitter', 'Help with homework required. Monday to Friday, 3PM-6PM.', '2025-11-04'),
(15, 'babysitter', 'Must be comfortable with pets. Saturday and Sunday only.', '2025-11-05'),
(16, 'caregiver for elderly', 'Experience with dementia patients essential. Soft-spoken and gentle approach needed.', '2025-11-06'),
(17, 'babysitter', 'Active caregiver who enjoys sports. After school care needed.', '2025-11-07'),
(18, 'playmate for children', 'Creative person for arts and crafts. Must be soft-spoken and encouraging.', '2025-11-08'),
(19, 'caregiver for elderly', 'Medical training required. Full day shifts available.', '2025-11-09'),
(20, 'babysitter', 'Experience with twins or multiple children preferred.', '2025-11-10'),
(21, 'caregiver for elderly', 'Post-surgery care experience needed. Physical strength required for mobility assistance.', '2025-11-11'),
(14, 'playmate for children', 'Looking for tutor/playmate combination. Must be patient.', '2025-11-12'),
(22, 'babysitter', 'Need someone reliable and punctual.', '2025-11-13'),
(22, 'caregiver for elderly', 'Looking for experienced elderly care professional.', '2025-11-14');

-- Insert JOB_APPLICATION records (15 applications)
INSERT INTO JOB_APPLICATION (caregiver_user_id, job_id, date_applied) VALUES
(1, 1, '2025-11-02'),
(4, 1, '2025-11-03'),
(7, 1, '2025-11-03'),
(2, 3, '2025-11-03'),
(5, 3, '2025-11-04'),
(8, 3, '2025-11-05'),
(1, 4, '2025-11-05'),
(7, 4, '2025-11-06'),
(3, 2, '2025-11-04'),
(6, 2, '2025-11-05'),
(9, 2, '2025-11-06'),
(2, 6, '2025-11-07'),
(5, 6, '2025-11-08'),
(1, 10, '2025-11-11'),
(4, 5, '2025-11-06');

INSERT INTO APPOINTMENT (caregiver_user_id, member_user_id, appointment_date, appointment_time, work_hours, status) VALUES
(1, 12, '2025-11-15', '09:00:00', 4, 'accepted'),
(2, 13, '2025-11-16', '10:00:00', 3, 'accepted'),
(3, 14, '2025-11-17', '15:00:00', 3, 'accepted'),
(4, 15, '2025-11-18', '14:00:00', 5, 'pending'),
(5, 16, '2025-11-19', '08:00:00', 6, 'accepted'),
(6, 17, '2025-11-20', '16:00:00', 2, 'declined'),
(7, 18, '2025-11-21', '13:00:00', 4, 'accepted'),
(8, 19, '2025-11-22', '09:00:00', 8, 'accepted'),
(9, 20, '2025-11-23', '10:00:00', 3, 'pending'),
(10, 21, '2025-11-24', '11:00:00', 5, 'accepted'),
(1, 14, '2025-11-25', '15:00:00', 3, 'accepted'),
(2, 16, '2025-11-26', '09:00:00', 4, 'accepted');


SELECT 'USER' AS table_name, COUNT(*) AS record_count FROM USER
UNION ALL
SELECT 'CAREGIVER', COUNT(*) FROM CAREGIVER
UNION ALL
SELECT 'MEMBER', COUNT(*) FROM MEMBER
UNION ALL
SELECT 'ADDRESS', COUNT(*) FROM ADDRESS
UNION ALL
SELECT 'JOB', COUNT(*) FROM JOB
UNION ALL
SELECT 'JOB_APPLICATION', COUNT(*) FROM JOB_APPLICATION
UNION ALL
SELECT 'APPOINTMENT', COUNT(*) FROM APPOINTMENT;
