from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from
from flask_cors import CORS
from elasticsearch import Elasticsearch
import requests

#Configure elasticsearch for keyword matching
es = Elasticsearch(hosts=["http://elasticsearch:9200"])
print(f"Connected to ElasticSearch cluster `{es.info()}`")

app = Flask(__name__)

CORS(app)
api = Api(app)

# Configuring Swagger API
app.config['SWAGGER'] = {
    'title': 'SEARCH API',
    'uiversion': 3
}
swagger = Swagger(app)

#Get a json copy of the dataset used
url = 'https://data.cityofchicago.org/resource/ygr5-vcbg.json?$limit=60'
response = requests.get(url)

json_data = response.json()

#Load json data into elastic search index
index_name = "cars"

#Delete Index API
delete_index_url = f"http://elasticsearch:9200/{index_name}"
response = requests.delete(delete_index_url)

# Check the response status
if response.status_code == 200:
    print(f"Index 'cars' successfully deleted.")
else:
    print(f"Failed to delete index. Response code: {response.status_code}, Response content: {response.text}")
    
# load data to elasticsearch index
for i in json_data:
        document = {
            "tow_date": i.get('tow_date', " ")  ,
            "make": i.get('make', " "),
            "style": i.get('style', " "),
            "color": i.get('color', " "),
            "plate": i.get('plate', " "),
            "inventory_number": i.get('inventory_number', " "),
            "towed_to_address": i.get('towed_to_address', " "),
        }
        es.index(index=index_name, document=document)


class Chicity_search(Resource):
    @swag_from("./yml/search.yml")
    def get(self):
        query = request.args["q"].lower()
        body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields":["plate", "make", "style", "color"] 
                }
            }
        }
        res = es.search(index="cars", body=body)
        return [result['_source'] for result in res['hits']['hits']]
    
api.add_resource(Chicity_search, '/item')
if __name__ == "__main__":
    app.run(debug=True)