from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/displayData')
def displayData():
    return render_template('displayData.html')

if __name__ == '__main__':
    app.run(port=33507)

