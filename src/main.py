"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


#Family Class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        #example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": "Doe",
                "age": "33",
                "genre": "Male",
                "lucky_numbers": "7, 13, 22"
            },
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": "Doe",
                "age": "33",
                "genre": "Male",
                "lucky_numbers": "7, 13, 22"
            },
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": "Doe",
                "age": "33",
                "genre": "Male",
                "lucky_numbers": "7, 13, 22"
            },
        ]




# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
