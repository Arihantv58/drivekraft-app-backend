-- creating db
create database drivekraft_backend;

-- creating user table
CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name Char(30),
        username CHAR(50) DEFAULT NUL,
        emailId CHAR(50),
        contact CHAR(20) NOT NULL,
        totalSessions int DEFAULT '0',
        firebase_id CHAR(100) DEFAULT NULL,
        firebase_name CHAR(100) DEFAULT NULL,
        firebase_email CHAR(100) DEFAULT NULL,
        firebase_password CHAR(100) DEFAULT NULL,
        credits INT DEFAULT 50,
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
        expiry_at DATE,
        updated_at DATE,
        created_at DATE
        )
