from flask import Flask, render_template, request, redirect

#Bokeh imports
from bokeh.plotting import figure
from bokeh.embed import components
import bokeh

import numpy as np
import pandas as pd
import quandl




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
        return redirect('/displayData')


@app.route('/displayData', methods=['GET','POST'])
def displayData():
    
    #Test Code
#    N=4000
#    x=np.random.random(size=N)*100
#    y=np.random.random(size=N)*100
#    radii=np.random.random(size=N)*1.5
#    colors = ["#%02x%02x%02x" % (r,g,150) for r,g in zip(np.floor(50+2*x),np.floor(30+2*y))]
#    p=figure()
#    p.circle(x,y,radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)
    #End test code
    
    #Download Data
    data = quandl.get("WIKI/AAPL")
    
    
    
    #Get Graph ready
    p1 = figure(x_axis_type="datetime", title="Stock Prices",plot_width=700, plot_height=500)
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'

    p1.line(data.index, data.Open, color='#A6CEE3', legend='Open')
    p1.line(data.index, data.Close, color='#B2DF8A', legend='Close')
    p1.line(data.index, data['Adj. Open'], color='#33A02C', legend='Ad. Open')
    p1.line(data.index, data['Adj. Close'], color='#FB9A99', legend='Ad. Close')
    p1.legend.location = "top_left"



    script, div = components(p1)


    
    return render_template('displayData.html', stock=app.vars['selectedStock'], testWord='WOW', script=script, div=div)

if __name__ == '__main__':
    app.run(port=33507, debug=True)

