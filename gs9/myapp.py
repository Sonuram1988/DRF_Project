import requests
import json

URL="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,data=json_data,headers=headers)
    data=r.json()
    print(data)

get_data()

def post_data():
    data={
        'name':'Vivan',
        'roll':110,
        'city':'Manipur'
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

# post_data()

def update_post():
    data={
        'id':6,
        'roll':104,
        'city':'Tohana'
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data,headers=headers)
    data=r.json()
    print(data)

# update_post()

def delete_data():
    data={'id':6}

    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

# delete_data()

    


