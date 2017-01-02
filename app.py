from flask import Flask, render_template, request, redirect

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
        #app_lulu.vars['name'] = request.form['name_lulu']
        #app_lulu.vars['age'] = request.form['age_lulu']
        


        app.vars['selectedStock'] = request.form['selectedStock']
        
        if request.form['TypeOfPrice_Open']==True:
            print "Open is clicked"
        if request.form['TypeOfPrice_Close'] == True:
            print "Close is clicked"
        #print request.form['TypeOfPrice_AO']
        #print request.form['TypeOfPrice_AC']
        
        return redirect('/displayData')

    
    


@app.route('/displayData', methods=['GET','POST'])
def displayData():
    
    

    
    return render_template('displayData.html', stock=app.vars['selectedStock'], testWord='WOW')

if __name__ == '__main__':
    app.run(port=33507, debug=True)

