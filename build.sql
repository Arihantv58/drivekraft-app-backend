-- creating db
create database drivekraft_backend;

-- creating user table
CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name Char(30),
        username CHAR(50) DEFAULT NULL,
        emailId CHAR(50),
        contact CHAR(20) NOT NULL,
        totalSessions int DEFAULT '0',
        firebase_id CHAR(100) DEFAULT NULL,
        firebase_name CHAR(100) DEFAULT NULL,
        firebase_email CHAR(100) DEFAULT NULL,
        firebase_password CHAR(100) DEFAULT NULL,
        credits INT DEFAULT 50,
        role_id INT DEFAULT 2,
        is_online INT DEFAULT 1,
        is_busy INT DEFAULT '0',
        created CHAR(50),
        updated CHAR(50)
        );

-- creating otp table
CREATE TABLE otp(
        id INT PRIMARY KEY AUTO_INCREMENT,
        userId CHAR(20),
        otpvalue INT,
        state ENUM('OTP_SEND','WRONG_OTP','CORRECT_OTP') DEFAULT 'OTP_SEND',
        created CHAR(50),
        updated CHAR(50)
        )

-- creating token table        
CREATE TABLE token(
        id INT PRIMARY KEY AUTO_INCREMENT,
        userId CHAR(20),
        tokenvalue CHAR(70),
        created CHAR(50),
        expireAt CHAR(50)
        )


-- creating sessionRequest table

-- creating token table
CREATE TABLE sessionRequest(
        id INT PRIMARY KEY AUTO_INCREMENT,
        listener_id CHAR(20),
        customer_id CHAR(20),
        is_cancelled  bool  DEFAULT false,
        status  bool  DEFAULT false,
        expiry_at DATETIME,
        updated_at DATETIME,
        created_at DATETIME
        );

-- creating role table
CREATE TABLE role(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name CHAR(20),
        label CHAR(20),
        created_at DATETIME,
        updated_at DATETIME
        );


-- inserting into role ids needed to be mapped properly
insert ignore into role values(2,'psychologist','Psychologist', now(),now())
insert ignore into role values(3,'customer','Customer', now(),now())


-- creating psychologist table
Create Table psychologist(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name CHAR(20),
        profile_image CHAR(20),
        is_busy bool  DEFAULT false,
        firebase_id CHAR(100) DEFAULT NULL,
        firebase_name CHAR(100) DEFAULT NULL,
        firebase_email CHAR(100) DEFAULT NULL,
        firebase_password CHAR(100) DEFAULT NULL,
        uuid CHAR(100),
        user_id CHAR(100),
        description LONGTEXT,
        session_count INT ,
        rating FLOAT ,
        yrs_of_exp INT,
        education CHAR(50),
        short_desc CHAR(200),
        status bool  DEFAULT true,
        order_ INT,
        updated_at DATETIME,
        created_at DATETIME,
        gender CHAR(20),
        age CHAR(20),
        interests CHAR(50),
        languages CHAR(40),
        online bool  DEFAULT true
    );



-- creating table paymentOrder
CREATE TABLE paymentOrder(
        id INT PRIMARY KEY AUTO_INCREMENT,
        order_id CHAR(100),
        payment_id CHAR(100),
        signature CHAR(100),
        amount CHAR(6),
        userId INT,
        paymentGateway CHAR(30),
        created_at DATETIME,
        updated_at DATETIME
        );


-- creating table transaction
CREATE TABLE transaction(
    id INT PRIMARY KEY AUTO_INCREMENT,
    transaction_id CHAR(100),
    userId INT,
    psychologist_id INT,
    session_request_id INT,
    seconds_chatted INT,
    amount_deducted INT,
    created_at DATETIME,
    updated_at DATETIME
);
