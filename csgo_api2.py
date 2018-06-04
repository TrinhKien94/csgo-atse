from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
from flask_cors import CORS
from sklearn.externals import joblib
clf = joblib.load('model.pkl')
app = Flask(__name__)
CORS(app)
api = Api(app)
def storeLog(log):
   hs = open("log20160602.txt","a")
   hs.write(log+ "\n")
   hs.close()

def convert_color(color):
    if color == 'red':
        return 2
    if color == 'black':
        return 1
    if color == 'green':
        return 0
def convert_number_to_color(number):
    if number == 2:
        return 'red'
    if number == 1:
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
        option = request.args.get('option')
        profit =request.args.get('profit')
        prev = request.args.get('prev')
        log = option + "|" + profit + "|" + prev
        log = log.replace(",","")
        log = log.replace("\n", "")
        log = log.replace("\s", "")
        print log
        storeLog(log)
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
        return {'predict': 'ok'} # Fetches first column that is Employee ID

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
     app.run(port=5003)
