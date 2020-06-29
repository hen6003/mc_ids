import requests, json
r = requests.get('https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/reports/registries/item/item.json')

ids_array = []

for i in r.json()['values']:
    ids_array.append(i[10:])

with open("ids.json", "w") as write_file:
    json.dump(ids_array, write_file)