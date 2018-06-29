from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
from flask_cors import CORS
from sklearn.externals import joblib
clf = joblib.load('model-roulette.pkl')
app = Flask(__name__)
CORS(app)
api = Api(app)
def storeLog(log):
   hs = open("log20160602-roulette.txt","a")
   hs.write(log+ "\n")
   hs.close()
def storeLogPercent(log,filename):
   hs = open(filename,"a")
   hs.write(log+ "\n")
   hs.close()
def convert_color(color):
    if color == 'red':
        return 1
    if color == 'black':
        return 2
    if color == 'green':
        return 0
def convert_number_to_color(number):
    if number == 1:
        return 'red'
    if number == 2:
        return 'black'
    if number == 0:
        return 'green'

def extract_feature(colors, values):
    number_before = 8
    color_nums = convert_data_color(colors)
    value_nums = conver_data_value(values)
    features = []
    for j in range(0,number_before):
        features.append(value_nums[j])
    for j in range(0,number_before):
        features.append(color_nums[j])
    count = 1
    for j in range(1, 10):
        if color_nums[0] == color_nums[j]:
            count += 1
        else:
            break
    features.append(count)
    return features

def conver_data_value(values):
    spl_values = values.split(',')
    converted_values = []
    for value in spl_values:
        converted_values.append(int(value))
    return converted_values

def convert_data_color(colors):
    spl_colors = colors.split(',')
    converted_colors = []
    for color in spl_colors:
        converted_colors.append(convert_color(color))
    return converted_colors

class Employees(Resource):
    def get(self):
        color = request.args.get('color')
        value =request.args.get('value')
        prev = request.args.get('prev')
        log = color + "|" + value + "|" + prev
        log = log.replace(",","")
        # print(log)
        storeLog(log)
        # log = log.replace("black\|\|green\|\|red\|","")
        log = log.replace("black","2")
        log = log.replace("red","1")
        log = log.replace("green","0")
        log = log.replace("2||0||1||","")
        print(log)
        inputStr = log.split('|')
        inputStr = inputStr[:len(inputStr)-2]
        inputStr = [int(x) for x in inputStr]
        features = []
        features.append(inputStr[0::2])
        predict = str(clf.predict(features)[0])
        # colors = request.args.get('colors')
        # values = request.args.get('values')
        # storeColor=colors.split(",")[0]
        # storeValue=values.split(",")[0]
        # # storeLog(storeColor+" "+storeValue)
        # print colors
        # print values
        # features = []
        # features.append(extract_feature(colors,values))
        # print features[0]
        # print "? "+str(clf.predict_proba(features)[0])
        # return {'predict': convert_number_to_color(clf.predict(features)[0])} # Fetches first column that is Employee ID
        return {'predict': predict} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        result = {'data': ['test']}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        result = {'data': ['test']}
        return jsonify(result)


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port=5001)
