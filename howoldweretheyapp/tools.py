import requests
import xmltodict
import json

def getcelebrityage():
    #get celebrity's age
    api_url = 'https://api.celebrityninjas.com/v1/search?name='
    name = 'mike myers'
    response = requests.get(api_url + name, headers={'X-Api-Key': 'zWquY7r4FJ1Zgc0e+JIYXA==0KvcDwW3scl3E0Tu'})
    if response.status_code == requests.codes.ok:
        print(type(response.json))
        celebrityinfo = json.loads(str(response.text))
        celebrityage = celebrityinfo[0]['age']
        if celebrityage is not None:
            print(celebrityage)
            return celebrityage
    else:
        print("Error:", response.status_code, response.text)

def getmediadata():
    print('placeholder')