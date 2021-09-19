from flask import Flask, render_template, url_for, jsonify, make_response
import logging 
import json 
 
app = Flask(__name__)

logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)
   
@app.route('/')
def hello_whale():
    endpoint = "Home Page"
    app.logger.info(f"{endpoint} endpoint was reached")
    return render_template("index.html")

@app.route('/test')
def test():
    endpoint = "Testing Page"
    app.logger.info(f"{endpoint} was reached")
    return render_template("test.html") 

@app.route('/status')
def health_check():
    endpoint = "Status"
    #return make_response(jsonify(data), status)
    
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status = 200,
        mimetype='application/json'
    )
    app.logger.info(f"{endpoint} was reached")
    return response

@app.route('/metrics')
def metrics():
    data = {"UserCount" : 140, "UserCountActive" : 23}
    endpoint = "Metrics"
#   return make_response(jsonify(data), status)
    response = app.response_class(
        response=json.dumps({"status":"success","code":0, "data":data}),
        status = 200,
        mimetype='application/json'
    )
    app.logger.info(f"{endpoint} was reached")
    return response
    
if __name__ == '__main__':
    app.run(debug=True,port=5000)
    
