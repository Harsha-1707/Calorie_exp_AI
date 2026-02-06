import requests
import json

url = 'http://127.0.0.1:5000/predict'
data = {
    "Gender": 0,
    "Age": 25,
    "Height": 170,
    "Weight": 70,
    "Duration": 30,
    "Heart_Rate": 100,
    "Body_Temp": 40
}

try:
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Success!")
        print("Response:", response.json())
    else:
        print(f"Failed with status {response.status_code}")
        print("Response:", response.text)
except Exception as e:
    print(f"Error: {e}")
