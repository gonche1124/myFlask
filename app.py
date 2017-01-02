from flask import Flask, render_template, request, redirect

#Bokeh imports
from bokeh.plotting import figure
from bokeh.embed import components
import bokeh

import numpy as np
import pandas as pd
import quandl
import requests



app = Flask(__name__)
app.vars={}

@app.route('/', methods=['GET','POST'])
def main():
    return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
    
    if request.method == 'GET':
        #return render_template('userinfo_lulu.html',num=nquestions)
        return render_template('index.html')
    else:
        #request was a POST
        app.vars['selectedStock'] = request.form['selectedStock']
        
        
        #Checkboxes
        app.vars['TypeOfPrice_Open']=request.form.getlist('TypeOfPrice_Open')
        app.vars['TypeOfPrice_Close']=request.form.getlist('TypeOfPrice_Close')
        app.vars['TypeOfPrice_AC']=request.form.getlist('TypeOfPrice_AC')
        app.vars['TypeOfPrice_AO']=request.form.getlist('TypeOfPrice_AO')
        
        return redirect('/displayData')


@app.route('/displayData', methods=['GET','POST'])
def displayData():
    
    #Download Data
    stock= app.vars['selectedStock']
    stock2download = "WIKI/%s" % stock
    data = quandl.get(stock2download)
    companyName= get_symbol(stock)
    
    #Get Graph ready
    p1 = figure(x_axis_type="datetime", title="Stock Prices",plot_width=700, plot_height=500)
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'
    
    #if not app.vars['TypeOfPrice_Open']:
    #    print "Opne is 1"
    #else:
    #    print type(app.vars['TypeOfPrice_Open'])
    
    #Add lines
    if len(app.vars['TypeOfPrice_Open'])==1:
        p1.line(data.index, data.Open, color='#A6CEE3', legend='Open')
    if len(app.vars['TypeOfPrice_Close'])==1:
        p1.line(data.index, data.Close, color='#B2DF8A', legend='Close')
    if len(app.vars['TypeOfPrice_AO'])==1:
        p1.line(data.index, data['Adj. Open'], color='#33A02C', legend='Ad. Open')
    if len(app.vars['TypeOfPrice_AC'])==1:
        p1.line(data.index, data['Adj. Close'], color='#FB9A99', legend='Ad. Close')

    p1.legend.location = "top_left"



    script, div = components(p1)


    
    return render_template('displayData.html', stock=companyName, script=script, div=div)

#Gets the company name based on a ticker
#Taken from "http://stackoverflow.com/questions/38967533/retrieve-company-name-with-ticker-symbol-input-yahoo-or-google-api"
def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
    
    result = requests.get(url).json()
    
    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']


if __name__ == '__main__':
    app.run(port=33507, debug=True)

