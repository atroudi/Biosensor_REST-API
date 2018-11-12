import hashlib
import json
import os
import sys
import requests

from urllib3 import request

from storeSecret import hash_secret

from flask import Flask, request, Response, jsonify
# from flask_httpauth import HTTPTokenAuth
from functools import wraps

from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
# from models import *


## GLOBAL
api_secret_hash_global = ''


# Configure mongodb
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bioSensors"
mongo = PyMongo(app)

# Configure postgres
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
POSTGRES = {
    'user': 'migiwara',
     'pw': 'root',
    'db': 'BiosensorsServer2',
    'host': '127.0.0.1',
    'port': '5432',
}
URI='postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
print(URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)
db.init_app(app)
db.Model.metadata.reflect(db.engine)

def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        api_secret = request.headers.get("Authorization")
        print(api_secret)
        # request.header.get("")
        # Update the global secret hash
        # global api_secret_hash_global
        # api_secret_hash_global = hash_secret(api_secret)

        # if api_secret == "asdasd":
        if api_secret == "cGF0aWVudDE6cWF0YXIxMjM=":
            return Response('Login!', 401, {'WWW-Authenticate': 'Basic realm="Login!"'})
        return f(*args, **kwargs)

    return wrapper

'''
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

	auth_header = request.headers.get('Api-Secret')
	print auth_header
	print request.headers
	return 'You want path: %s' % path
'''

'''
@POST("entries")
Call<ResponseBody> upload(@Header("api-secret") String secret, @Body RequestBody body);
'''


@app.route('/api/v1/entries', methods=['POST'])
# @authenticate
def post_entries():
    print("HEADERS:\n" , request.headers)

    print("ARGUMENTS:\n" ,request.args)
    print("JSON:\n" ,request.json)

    global api_secret_hash_global
    # Append secret to entry
    dictSecret={"api_secret": api_secret_hash_global}

    # Get name associated with secret from Postfres
    ## NOW IS HARDCODED
    dictName={"username": "AnisTroudi"}

    dictEntry=request.json
    # merge dictionaries
    mergedDict = dictSecret.copy()
    mergedDict.update(dictName)
    mergedDict.update(dictEntry)

    # Store entry in mongodb
    mongo.db.entries.insert(mergedDict)
    # Store entry in Postgres
    message = "Stored entry!"

    email=request.args.get('email')
    password=request.args.get('password')
    url= 'http://'+ email +':'+ password + '@localhost:8000/api/v1/entries/'
    print ('URL: ',url)
    # store the data in postgres
    res = requests.post( url, json=request.json)

    return jsonify(message)

'''
@POST("devicestatus")
Call<ResponseBody> uploadDeviceStatus(@Header("api-secret") String secret, @Body RequestBody body);
'''


@app.route('/api/v1/devicestatus', methods=['POST'])
def post_devicestatus():
    print(request.args)
    print(request.json)

    return "{}"


'''
@GET("status.json")
Call<ResponseBody> getStatus(@Header("api-secret") String secret);
'''


@app.route('/api/v1/status.json', methods=['POST'])
def get_status():
    print(request.args)
    print(request.json)

    return "{}"


'''
@POST("treatments")
Call<ResponseBody> uploadTreatments(@Header("api-secret") String secret, @Body RequestBody body);
'''


@app.route('/api/v1/treatments', methods=['POST'])
def post_treatments():
    print(request.args)
    print(request.json)

    return "{}"


'''
@PUT("treatments")
Call<ResponseBody> upsertTreatments(@Header("api-secret") String secret, @Body RequestBody body);
'''


@app.route('/api/v1/treatments', methods=['PUT'])
def put_treatments():
    print(request.args, file=sys.stdout)
    print(request.json)

    return "{}"


'''
@GET("treatments")
// retrofit2/okhttp3 could do the if-modified-since natively using cache
Call<ResponseBody> downloadTreatments(@Header("api-secret") String secret, @Header("BROKEN-If-Modified-Since") String ifmodified);
'''


@app.route('/api/v1/treatments', methods=['GET'])
@authenticate
def get_treatments():
    print("get_treatments")
    print(request)
    print(request.json)

    return "{}"


'''
@GET("treatments.json")
Call<ResponseBody> findTreatmentByUUID(@Header("api-secret") String secret, @Query("find[uuid]") String uuid);
'''


@app.route('/api/v1/treatments.json/<uuid>', methods=['GET'])
def get_treatment(uuid):
    print(request.args)
    print(request.json)

    return "{}"


'''
@DELETE("treatments/{id}")
Call<ResponseBody> deleteTreatment(@Header("api-secret") String secret, @Path("id") String id);
'''


@app.route('/api/v1/treatments.json/<id>', methods=['DELETE'])
def delete_treatments(uuid):
    print(request.args)
    print(request.json)

    return "{}"


'''
@POST("activity")
Call<ResponseBody> uploadActivity(@Header("api-secret") String secret, @Body RequestBody body);
'''


@app.route('/api/v1/activity', methods=['POST'])
def post_activity():
    print(request.args)
    print(request.json)

    return "{}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
