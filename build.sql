-- creating db
create database drivekraft_backend;

-- creating user table
CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name Char(30),
        username CHAR(50),
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


{
    "msg": "Successfully Updated.",
    "status": "Success",
    "user": {
        "id": 3,
        "username": "draft",
        "uuid": null,
        "name": null,
        "profile_image": "users/default.png",
        "mobile": "918284990439",
        "email": null,
        "email_verified_at": null,
        "otp": "108286",
        "otp_expires_at": "2023-08-29 01:08:52",
        "country": null,
        "timezone": "Asia/Kolkata",
        "created_at": "2023-05-21T05:27:49.000000Z",
        "updated_at": "2023-08-28T19:31:25.000000Z",
        "google_id": null,
        "avatar": null,
        "stripe_id": null,
        "pm_type": null,
        "pm_last_four": null,
        "trial_ends_at": null,
        "deleted_at": null,
        "device_id": null,
        "device_token": null,
        "firebase_id": "abcd",
        "firebase_name": "efgh",
        "firebase_email": "ijkl",
        "firebase_password": "mnop",
        "credits": 90,
        "online": 0,
        "is_busy": 0
    }
}