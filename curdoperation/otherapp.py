import requests
import json

# URL = "http://127.0.0.1:8000/stuinfo/"
# req = requests.get(url = URL)
# data = req.json()
# print(data)

# URL = "http://127.0.0.1:8000/stucreate/"
# data = {
#     'id' : 5,
#     'name' : 'shalini',
#     'roll' : 101,
#     'city' : 'jhansi',
# }
# json_data = json.dumps(data)
# r = requests.post(url = URL, data = json_data)
# data = r.json()
# print(data)

URL =  "http://127.0.0.1:8000/api/crud/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    req = requests.get(url = URL, data = json_data)
    data = req.json()
    print(data)

# get_data(51)

def post_data():
    data = {
        'id' : 57,
        'name' : 'Dev',
        'email' : 'dev@gmail.com',
        'password' : 'dev',
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id' : 57,
        'name' : 'ritin sahu',
        'roll' : 203,
        'city' : 'jhansi',
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {
        'id' : 57
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

# delete_data()