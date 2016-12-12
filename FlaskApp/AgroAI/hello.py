"""Cloud Foundry test"""
from flask import Flask
import cf_deployment_tracker
from flask import render_template
from flask import request
import os
from Machines import model1
from Machines import model2

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/model1', methods=['POST'])
def predict_irrigation():

    request_data = request.json
    countyname = request_data['countyname']
    typeofplant = request_data['typeofplant']

    response = model1.model1(countyname=countyname, typeOfPlant=typeofplant)
    return response


@app.route('/model2', methods=['POST'])
def predict_crop():

    request_data = request.json
    print request_data
    countyname = request_data['countyname']
    area = request_data['area']

    response = model2.model2(inputCounty=countyname, area=area)
    return  response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

