-- creating db
create database drivekraft_backend;

-- creating user table
CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name Char(30),
        emailId CHAR(50),
        contact CHAR(20) NOT NULL,
        totalSessions int DEFAULT '0',
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


