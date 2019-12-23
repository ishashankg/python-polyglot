import flask
from flask import request
from utils import checkPrime

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# API End point : localhost:5000/api/prime?number=3797
@app.route('/api/prime', methods=['GET'])
def prime():
    params = request.args
    number = params.get("number")
    return checkPrime(number)


app.run()
