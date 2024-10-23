import requests

url = "http://127.0.0.1:8080/predict"
data = {"size": 100, "bedrooms": 3, "garden": 1}
response = requests.post(url, json=data)
print(response.json())