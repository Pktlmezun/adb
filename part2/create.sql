CREATE TABLE USER (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    given_name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    profile_description TEXT,
    password VARCHAR(255) NOT NULL
);


CREATE TABLE CAREGIVER (
    caregiver_user_id INT PRIMARY KEY,
    photo VARCHAR(255),
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    caregiving_type ENUM('babysitter', 'caregiver for elderly', 'playmate for children') NOT NULL,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (caregiver_user_id) REFERENCES USER(user_id) ON DELETE CASCADE
);


CREATE TABLE MEMBER (
    member_user_id INT PRIMARY KEY,
    house_rules TEXT,
    dependent_description TEXT,
    FOREIGN KEY (member_user_id) REFERENCES USER(user_id) ON DELETE CASCADE
);


CREATE TABLE ADDRESS (
    member_user_id INT PRIMARY KEY,
    house_number VARCHAR(20) NOT NULL,
    street VARCHAR(255) NOT NULL,
    town VARCHAR(100) NOT NULL,
    FOREIGN KEY (member_user_id) REFERENCES MEMBER(member_user_id) ON DELETE CASCADE
);


CREATE TABLE JOB (
    job_id INT PRIMARY KEY AUTO_INCREMENT,
    member_user_id INT NOT NULL,
    required_caregiving_type ENUM('babysitter', 'caregiver for elderly', 'playmate for children') NOT NULL,
    other_requirements TEXT,
    date_posted DATE NOT NULL,
    FOREIGN KEY (member_user_id) REFERENCES MEMBER(member_user_id) ON DELETE CASCADE
);


CREATE TABLE JOB_APPLICATION (
    caregiver_user_id INT NOT NULL,
    job_id INT NOT NULL,
    date_applied DATE NOT NULL,
    PRIMARY KEY (caregiver_user_id, job_id),
    FOREIGN KEY (caregiver_user_id) REFERENCES CAREGIVER(caregiver_user_id) ON DELETE CASCADE,
    FOREIGN KEY (job_id) REFERENCES JOB(job_id) ON DELETE CASCADE
);


CREATE TABLE APPOINTMENT (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    caregiver_user_id INT NOT NULL,
    member_user_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    work_hours INT NOT NULL,
    status ENUM('pending', 'accepted', 'declined') NOT NULL,
    FOREIGN KEY (caregiver_user_id) REFERENCES CAREGIVER(caregiver_user_id) ON DELETE CASCADE,
    FOREIGN KEY (member_user_id) REFERENCES MEMBER(member_user_id) ON DELETE CASCADE
);
