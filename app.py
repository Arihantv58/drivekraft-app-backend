from flask import Flask,jsonify
import logging
import json
import configuration.logfileConfigs as logfileConfigs
import otp.otpService as otpService
import user.userService as userService
import role.roleService as roleService
import psychologist.psychologistService as psychologistService
import sessionRequest.sessionRequestService as sessionRequestService
import payment.paymentService as paymentService


app = Flask(__name__)
logfileConfigs.logFileCongig()


@app.route("/")
def index():
    logging.info("testt")
    return "test"


@app.route("/api/login-send-otp",methods=['POST'])
def sendOtp():
    return otpService.sendOtpInternally()

@app.route("/api/login",methods=['POST'])
def generateToken():
    return otpService.generateTokenInternally()


@app.route("/api/user/firebase", methods =['POST'])
def getUSerForFirebase():
    return userService.firebaseUser()


@app.route("/api/user", methods =['GET'])
def getUSer():
    user=userService.getUser()
    return jsonify({
        "user": json.dumps(user.__dict__)
    })


@app.route("/api/username/check", methods =['POST'])
def checkUserNameIfExists():
    return userService.checkUsername()

@app.route("/api/session/book/request", methods =['POST'])
def bookRequest():
        return sessionRequestService.sendSessionRequest()


@app.route("/api/session/book/request/cancel", methods =['POST'])
def cancelSessionRequest():
        return sessionRequestService.cancelSessionRequest()

@app.route("/api/session/book/request/verify", methods =['POST'])
def verifySessionRequest():
        return sessionRequestService.verifySessionRequest()


@app.route("/api/session/request/confirm", methods =['POST'])
def confirmSessionRequestInternal():
        return sessionRequestService.confirmSessionRequest()


@app.route("/api/role", methods =['GET'])
def getRole():
        return roleService.getUserRole()


@app.route("/api/psychologists", methods =['GET'])
def getPsychologist():
        data= psychologistService.getPsychologistList()
        return ({
            "data": str(data)
        })

@app.route("/api/order/create", methods =['POST'])
def createRazorpayOrder():
    response= paymentService.createRazorpayOrder()
    return ({
        "order_id": response['id'],
        "currency" : "INR" ,
        "amount" : response['amount']/100
    })

app.run(debug=True)


