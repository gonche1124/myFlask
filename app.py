from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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
        
        #f = open('%s_%s.txt'%(app_lulu.vars['name'],app_lulu.vars['age']),'w')
        #f.write('Name: %s\n'%(app_lulu.vars['name']))
        #f.write('Age: %s\n\n'%(app_lulu.vars['age']))
        #f.close()
        
        stockSelected = request.form['selectedStock']
        return render_template('displayData.html', stock=stockSelected)
    
    


#@app.route('/displayData')
#def displayData():
#    return render_template('displayData.html')

if __name__ == '__main__':
    app.run(port=33507)

