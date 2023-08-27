from flask import Flask
from configuration import logfileConfigs
from otp import otpService 
import logging




app = Flask(__name__)
logfileConfigs.logFileCongig()


@app.route("/")
def index():
    logging.info("testt")
    return "test"


@app.route("/api/login-send-otp",methods=['POST'])
def sendOtp():
    return otpService.sendOtpInternally()

app.run(debug=True)


