import requests
import json
url = 'http://127.0.0.1:5000'
data = {"Pclass": 3, "Age": 2, "SibSp": 1, "Fare": 50}
response = requests.post(url, json.dumps(data))
print(response.json())
