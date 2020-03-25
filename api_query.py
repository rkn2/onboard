import requests

# curl2python: https://curl.trillworks.com/#python

#login
url = 'https://api.onboarddata.io/login/api-key'
key = "ob-p-VJqnaGrdsEX4LS9LOxdG2a-4sHnVAlVC976lnOnr9Lq8eLbIMff66HCa6IgT0XdSC-s"
r = requests.post(url, {"key": key})

# get list of buildings
headers = {
    'accept': 'application/json',
    'X-OB-Api': key
}
building_url = 'https://api.onboarddata.io/buildings'
building_list = requests.get(building_url, headers=headers)

# get equipment by building
params = (
    ('points', 'true'),
    ('datasource_hashes', '\'5ca742e59ac6fcfb47ce1438f2c04bf9\''),
    ('no_data', 'true'),
)
equipment_list = requests.get('https://api.onboarddata.io/buildings/38/equipment?points=true', headers=headers)

# get points by building_id
response = requests.get('https://api.onboarddata.io/buildings/38/points?no_data=true', headers=headers)

