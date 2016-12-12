


"""Cloud Foundry test"""
from flask import Flask
#import cf_deployment_tracker
from flask import render_template
from flask import request
import os
from Machines import model1
from Machines import model2
from Machines import model3
from Machines import model4
from Machines import userdata
from flask import send_from_directory
# Emit Bluemix deployment event
#cf_deployment_tracker.track()

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 5000))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/loadIt', methods=['POST'])
def load_data():
    print("I am here")
    request_data = request.form
    print(request_data)
    return "You finally got here"






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


@app.route('/model3', methods=['POST'])
def predict_crop_nonirr():

    request_data = request.json
    print request_data
    countyname = request_data['countyname']
    area = request_data['area']

    response = model3.model3(inputCounty=countyname, area=area)
    return response

@app.route('/model4', methods=['POST'])
def predict_windbreak():

    request_data = request.json
    print request_data
    countyname = request_data['countyname']

    response = model4.model4(inputCounty=countyname)
    return response

@app.route('/userdata', methods=['POST'])
def get_user_data():
    request_data = request.json

    response = userdata.import_userdata(request_data)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
