import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle



# create df
train = pd.read_csv('train.csv') # change file path
# drop null values
train.dropna(inplace=True)
# features and target
target = 'Survived'
features = ['Pclass', 'Age', 'SibSp', 'Fare']
# X matrix, y vector
X = train[features]
y = train[target]
# model 
model = LogisticRegression()
model.fit(X, y)
model.score(X, y)

pickle.dump(model, open('model.pkl', 'wb'))

# from flask import Flask, jsonify, request
# import requests
# import json

# # local url
# url = 'http://127.0.0.1:5000'

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