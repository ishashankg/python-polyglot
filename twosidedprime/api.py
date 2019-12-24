import flask
from flask import request
from utils import check_prime

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# API End point : localhost:5000/api/prime?number=3797
@app.route('/api/prime', methods=['GET'])
def prime():
    params = request.args
    number = params.get("number")
    return check_prime(number)


app.run()
