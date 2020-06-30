from datetime import date as dt
# from datetime import datetime as dtm
##import datetime #import datetime
from flask import Flask, render_template
import pandas as pd
import requests
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.figure as Figure
from flask import Response

class siteUtils():

    def joinHTTP(*args):
        return ('/').join(args)


    def main():
        countries = ["Poland", "United States of America", "Romania", "Uganda", "Eritrea"]
        avgDeathsDict = dict()
        updatesCountriesDict = dict()
        dataFormat = '%Y-%m-%d'
        httpBase = 'https://api.covid19api.com/country/'
        startDate = '2020-02-01'

        endDate = dt.today().strftime('%Y-%m-%d')

        countries_request = [requests.get(joinHTTP(httpBase, value)) for (value) in countries]
        countries_frame = [pd.read_json(countries_request[i].content) for i in range(0, len(countries))]

        for i in range(len(countries)):
            avgDeathsDict[countries[i]] = countries_frame[i].Deaths
            # updatesCountriesDict[cntrs[i]] = [datetime.datetime.strptime(element, dataFormat).date() for element in countries_frame[i].Date]
            updatesCountriesDict[countries[i]] = countries_frame[i].Date

        plt.bar(updatesCountriesDict["Romania"], avgDeathsDict["Romania"])
         plt.xticks(rotation=45)
        plt.title("Rumunia")
        plt.xlabel("xx")
        plt.ylabel("xxx [xx]")
        plt.legend(["xxxx"])
        plt.grid()
        plt.show()

    if __name__ == '__main__':
        main()


app=Flask(__name__)
utils=SiteUtils()

@app.route('/powitanie')
def home():
    return "Witam na moim API!"

@app.route('/powitanie/<string:name>')
def hello_you(name):
    return "Witam serdecznie, " + name

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/Zgony.html')
def active():
    return render_template('Deaths.html')

@app.route('/plot.png')
def plot_png():
    # Tworzę obrazek z wykresu
    fig = utils.create_figure()
    # Skomplikowany proces pzerobienia na plik .png
    output=io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')



app.run(debug=True)