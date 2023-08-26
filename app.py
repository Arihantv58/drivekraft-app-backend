from flask import Flask
from configuration import logfileConfigs




app = Flask(__name__)
logfileConfigs.logFileCongig()


@app.route("/")
def index():
    return "test"


app.run(debug=True)


