import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"
data = {
    'id':2,
    'name':'shubham',
    'roll':86,
    'city':'indore'
}

json_data = json.dumps(data)
r = requests.post(URL,json_data)

d = r.json()
print(d)