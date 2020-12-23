
from flask import Flask, render_template, url_for
 
app = Flask(__name__)
  
   
@app.route('/')
def hello_whale():
    return render_template("index.html")

@app.route('/test')
def test():
    return render_template("test.html") 

@app.route('/health')
def heathy():
    return 'I am Healthy!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
