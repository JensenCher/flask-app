# from flask import Flask, jsonify, request
# import requests
# import json

# # local url
# heroku_url = "https://titanic-flask-model-js.herokuapp.com/"

# # test data
# data = {  'Pclass': 3
#              , 'Age': 2
#              , 'SibSp': 1
#              , 'Fare': 50}

# data = json.dumps(data)
# print(data)


# # send_request = requests.post(heroku_url, data)
# # print(send_request)
# # print(send_request.json())

# r_survey = requests.post(heroku_url, data)
# print(r_survey)

# send_request = requests.post(heroku_url, data)
# print(send_request)

# print(send_request.json())


# from flask import Flask, jsonify, request
# import requests
# import json

# # local url
# url = 'https://titanic-flask-model-js.herokuapp.com/'

# # test data
# data = {  'Pclass': 3
#              , 'Age': 2
#              , 'SibSp': 1
#              , 'Fare': 50}

# data = json.dumps(data)
# print(data)


# r_survey = requests.post(url, data)
# print(r_survey)

# send_request = requests.post(url, data)
# print(send_request)

# print(send_request.json())


import requests
import json
import pandas as pd
url = 'https://titanic-flask-model-js.herokuapp.com/'
data = {"Pclass":3, "Age":2, "SibSp":1, "Fare":50}
response = requests.post(url, json.dumps(data))
data.update((x, [y]) for x, y in data.items())
print(data)
data_df = pd.DataFrame.from_dict(data)
print(data_df)
# print(response.json())