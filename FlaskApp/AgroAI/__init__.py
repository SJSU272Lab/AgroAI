from flask import Flask
from flask import render_template
from flask import request



app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/loadIt', methods=['POST'])
def load_data():
    print("I am here")
    request_data = request.form
    print(request_data)
    return "You finally got here"

if __name__ == "__main__":
    app.run(threaded=True)
