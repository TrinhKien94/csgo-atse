from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
from flask_cors import CORS
from sklearn.externals import joblib
import datetime
clf = joblib.load('model-coinflip.pkl')
app = Flask(__name__)
CORS(app)
api = Api(app)
def storeLog(log):
   hs = open("log20160602.txt","a")
   hs.write(log+ "\n")
   hs.close()

def storeLogBunny(log):
   hs = open("bunny.txt","a")
   hs.write(log+ "\n")
   hs.close()

def storeLogPredict(predict):
   hs = open("predict.txt","a")
   hs.write(predict+" ")
   hs.close()


def storeLogTruth(predict):
   hs = open("predict.txt","a")
   hs.write(predict+'\n')
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

def convert_1_2(number):
    if number == '1':
        return '2'
    if number == '2':
        return '1'

def storeLogPercent(log,filename):
   hs = open(filename,"w")
   hs.write(log)
   hs.close()

def readLogPercent(filename):
    hs = open(filename, "r")
    line = hs.readline()
    data = line.split('|')
    hs.close()
    if len(data) < 2 or data[1]=='0':
        return 0, 0
    return int(data[0]), int(data[1])

class Employees(Resource):
    def get(self):
        option = request.args.get('option')
        profit =request.args.get('profit')
        prev = request.args.get('prev')
        if option is not None:
            log = option + "|" + profit + "|" + prev
            log = log.replace(",","")
            log = log.replace("\n", "")
            log = log.replace("\s", "")
            storeLog(log)
            steamId= request.args.get('steam_id')
            if int(profit) < 0:
                option = convert_1_2(option)
            log = option + "|" + profit + "|" + prev
            log = log.replace(",","")
            log = log.replace("\n", "")
            log = log.replace("\s", "")
            inputStr = log.split('|')
            if steamId == '76561198052823882':
                time = str(datetime.datetime.now())
                log = time +"|"+log
                storeLogBunny(log)
            win, total = readLogPercent("percent.txt")
            if int(profit) > 0:
                win+=1
            total+=1
            percent = 0
            if total!=0:
                percent = 100.0 * float(win) / float(total)
            storeLogPercent(str(win)+"|"+str(total),"percent.txt")
            print("|".join(inputStr[0::2]))
            inputStr = inputStr[:len(inputStr)-2]
        else:
            prev = prev.replace(",","")
            prev = prev.replace("\n", "")
            prev = prev.replace("\s", "")
            inputStr = prev.split('|')
        print(inputStr)
        inputStr = [int(x) for x in inputStr]
        features = []
        features.append(inputStr[0::2])
        predict = str(clf.predict(features)[0])
        print(predict)
        if option is not None:
            storeLogTruth(option)
        storeLogPredict(predict)
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
        # return {'predict': clf.predict(features)} # Fetches first column that is Employee ID
        if option is not None:
            return {'predict': predict,'percent':percent,"total":total}
        else:
            return {'predict': predict}
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
