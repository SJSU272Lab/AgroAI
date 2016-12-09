"""Cloud Foundry test"""
from flask import Flask
import cf_deployment_tracker
from flask import render_template
from flask import request
import os

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))


@app.route('/')
def homepage():
    return render_template("homepage.html")

#@app.route('/')
#def hello_world():
#    return 'Hello World! I am running on port ' + str(port)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
    




#
#@app.route('/loadIt', methods=['POST'])
#def load_data():
#    print("I am here")
#    request_data = request.form
#    print(request_data)
#    return "You finally got here"



