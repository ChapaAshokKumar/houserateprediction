import requests

url = "https://houserateprediction-fmsp.onrender.com/ratepredict"

data = {
    "area":2600,
    "bed_rooms":3,
    "age":7
}

res = requests.post(url,json=data)
print(res.json())