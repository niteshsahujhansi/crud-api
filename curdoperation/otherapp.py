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
    # json_data = json.dumps(data)
    # req = requests.get(url = URL, data = json_data)
    req = requests.get(url = URL, data = data)
    data = req.json()
    print(data)

# get_data()

def post_data():
    data = {
        'id' : '57',
        'name' : 'rani',
        'email' : 'rani@gmail.com',
        'password' : 'rani',
    }
    # json_data = json.dumps(data)
    r = requests.post(url = URL, data = data)
    # r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id' : '66',
        'name' : 'nitin',
        'email' : 'nitin@gmail.com',
        'password' : 'nitin',
    }
    # json_data = json.dumps(data)
    r = requests.put(url = URL, data = data)
    # r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

update_data(66)

def delete_data():
    data = {
        'id' : 66
    }
    # json_data = json.dumps(data)
    r = requests.delete(url = URL, data = data)
    data = r.json()
    print(data)

# delete_data()