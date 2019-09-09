# run ngrok ==> ngrok http 5000
from flask import Flask, request, make_response, jsonify
import time
import random as rand

app = Flask(__name__)

def results():
    x = rand.uniform(0.2, 2.5)
    print ("incoming request...")
    print("delay for "+str(x)+" seconds")
    time.sleep(x)
    req = request.get_json(force=True)
    id = req.get('queryResult').get('intent')
    id = id.get('displayName')
    print ("call for intent: "+id)
    if (id == "got_pain"):
        x = 'Kannst du mir deine Symptome etwas genauer schildern'
        return {'fulfillmentText': 'Kannst du mir deine Symptome etwas genauer schildern?'}
    elif (id == "get_name"):
        name = req.get('queryResult').get('parameters')
        name = name.get('vorname')
        time.sleep(1)
        if (name == "Georg"):
            return {'fulfillmentText': 'Georg ist ein scheiss Name'}
        return {'fulfillmentText': 'Hallo '+name+', wie kann ich dir helfen?'}
    elif (id == "get_name - no - custom"):
        return {'fulfillmentText': 'Kannst du mir deine Symptome etwas genauer schildern?'}

    else:
        return {'fulfillmentText': ''}

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/webhook', methods = ['POST'])
def webhook():
    return make_response(jsonify(results()))


if __name__ == '__main__':
    app.run()
