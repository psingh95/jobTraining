import json
import pandas as pd

lake = pd.read_csv('addresses.csv')
print(lake['Last'])

""" with open('ex.json') as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
lakers 
print(jsonObject["array"][0]['age']) """    