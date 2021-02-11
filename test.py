from flask import Flask, jsonify, request
import requests
import json

# local url
heroku_url = "https://titanic-flask-model-js.herokuapp.com/"

# test data
data = {  'Pclass': 3
             , 'Age': 2
             , 'SibSp': 1
             , 'Fare': 50}

data = json.dumps(data)
print(data)


send_request = requests.post(heroku_url, data)
print(send_request)
print(send_request.json())

# r_survey = requests.post(url, data)
# print(r_survey)

# send_request = requests.post(url, data)
# print(send_request)

# print(send_request.json())