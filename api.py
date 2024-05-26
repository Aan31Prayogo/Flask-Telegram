from flask import Flask, jsonify, request
import requests
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message":"Hello World"})

@app.route("/send/text", methods = ['POST'])
def send_text_to_telegram():
    res = {}
    try:
        param = request.json        
        token = param['token']
        
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        param.pop('token')
        resp = requests.post(url, json= param)
        
        resp_json = resp.json()
        resp_json['isSuccess'] = True
        
        return jsonify(resp_json),200
    except Exception as e:
        res['isSuccess'] = False
        res['message'] = str(e)
        return jsonify(res),500
        

@app.route("/send/image", methods = ['POST'])
def send_image_to_telegram():
    res = {}
    try:
        param = request.json        
        TOKEN = param['token']
        CHAT_ID =  param['chat_id']
        url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}'
        
        image = open(sys.path[0] +'/image.jpg', 'rb') 
        print(image)               
        resp = requests.post(url, files={'photo':image})
        
        resp_json = resp.json()
        resp_json['isSuccess'] = True
        
        return jsonify(resp_json),200
    except Exception as e:
        res['isSuccess'] = False
        res['message'] = str(e)
        return jsonify(res),500
        
    

if __name__ == '__main__':
    app.run()