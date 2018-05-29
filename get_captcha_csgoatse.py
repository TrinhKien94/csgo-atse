from flask import Flask, request
from flask import json
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
import urllib
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)

# @app.route('/get_image', methods = ['POST'])
# def get_image(self):
#     if request.headers['Content-Type'] == 'text/plain':
#         print "Text Message: " + request.data
#
#     elif request.headers['Content-Type'] == 'application/json':
#         print "JSON Message: " + json.dumps(request.json)
#     # image_url = request.args.get('image')
#     # print image_url
#     # count = request.args.get('count')
#     # print count
#     # urllib.urlretrieve(image_url,"captcha"+count+".jpg")


@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        data = json.loads(request.data)
        print data
        print data.image
        print data.count
        # return "Text Message: " + request.dataType

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
     app.run(port=5002)
