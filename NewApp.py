import pandas as pd
import requests
from datetime import date as dt
from matplotlib import pyplot as plt


def joinHTTP(*args):
    return ('/').join(args)

countries = { "Kiribati", "Romania", "Uganda", "Bermuda", "Eritrea", "French Guiana", "Turks and Caicos Islands",
   "Bahamas", "Iceland", "Kyrgyzstan", "Puerto Rico", "Saint Helena", "Costa Rica", "Guadeloupe", "Cayman Islands",
   "Slug": "cayman-islands", "Gabon", "Czech Republic", "Serbia", "Western Sahara" }


httpBase = 'https://api.covid19api.com/country/'
startDate = '2020-01-01'
endDate = dt.today().strptime('%Y-%m-%d')

countires_request = [requests.get(joinHTTP(httpBase,value,key,startDate,endDate)) for (key,value) in countries.items()]

countires_frame = [pd.read_json(countires_request[i].content) for i in range(0,len(countires))]

cntrs = ["Kiribati", "Romania", "Uganda", "Bermuda", "Eritrea", "French Guiana", "Turks and Caicos Islands",
   "Bahamas", "Iceland", "Kyrgyzstan", "Puerto Rico", "Saint Helena", "Costa Rica", "Guadeloupe", "Cayman Islands",
   "Slug": "cayman-islands", "Gabon", "Czech Republic", "Serbia", "Western Sahara"]

avgDeathsDict = dict()
updatesCountriesDict = dict()
dataFormat = '%Y-%m-%d'

for i in range(len(cntrs)):
    avgDeathsDict[cntrs[i]] = [element['Deaths'] for element in countries_frame[i].rates]
    updatesCountriesDict[cntrs[i]] = [datetime.datetime.strptime(element['Date'],dataFormat).date() for element in countries_frame[i].rates]
#updatesCurrenciesDict.keys()
#updatesCurrenciesDict['USD']


plt.plot(updatesCountriesDict["Romania"], avgDeathsDict["Romania"])
plt.xticks(rotation=45)
plt.title("Rumunia")
plt.xlabel("xx")
plt.ylabel("xxx [xx]")
plt.legend(["xxxx"])
plt.grid()
plt.show()

