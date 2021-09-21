import json

f = open('ex.json')

data = json.load(f)
print(data['collection'][0]['id'])