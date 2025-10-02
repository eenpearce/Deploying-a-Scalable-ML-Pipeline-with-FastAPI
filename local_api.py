# import json

import requests

# TODO: send a GET using the URL http://127.0.0.1:8000
url = "http://127.0.0.1:8000"

r = requests.get(url)

# Print the status code
print("GET Status Code:", r.status_code)

# Print the welcome message (response body)
print("GET Result:", r.text)


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
r = requests.post(f"{url}/data/", json=data)

# Print the status code
print("POST Status Code:", r.status_code)

# Print the result from the POST request
print("POST Result:", r.json())
