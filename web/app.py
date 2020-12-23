
from flask import Flask, render_template, url_for
 
app = Flask(__name__)

count = 0 

@app.route('/')
def hello_whale():
    global count
    if count < 5:
        count += 1
        return render_template("index.html")
    else:
        return "Record not found", 400
@app.route('/test')
def test():
    return render_template("test.html") 

@app.route('/health')
def heathy():
    return 'I am Healthy!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    
