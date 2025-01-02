from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
api = Api(app)

# Configuring Swagger API
app.config['SWAGGER'] = {
    'title': 'SEARCH API',
    'uiversion': 3
}
swagger = Swagger(app)

if __name__ == "__main__":
    app.run(debug=True)
