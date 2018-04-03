import csv
import pickle
from collections import OrderedDict

colors = [0,0,0]
feat_color = OrderedDict()

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

# Load data tu CSV file
def load_data(filename):
   lines = csv.reader(open(filename, "rb"), delimiter=',')
   dataset = list(lines)
   for i in range(len(dataset)):
       dataset[i] = [int(x) for x in dataset[i]]
   return dataset


def get_data_label(dataset):
    data = []
    label = []
    for x in dataset:
        data.append(x[1:])
        label.append(x[0])
    return data, label

def count_feat_color_case(feat_num,feat,color):
    key = str(feat_num)+'|'+str(feat) +'|'+ str(color)
    if key in feat_color:
        feat_color[key]+=1
    else:
        feat_color[key]=1

def count_color(color):
    colors[color]+=1

# trainingSet = load_data('training.csv')
trainingSet = load_data('training2.csv')
dataTrain, labelTrain = get_data_label(trainingSet)

# for label in labelTrain:
#     count_color(label)
# lenL = len(labelTrain)
# lenD = len(dataTrain[0])
# for i in range(0, lenL):
#     for j in range(0, lenD):
#         count_feat_color_case(j,dataTrain[i][j],labelTrain[i])
# print colors
# print feat_color
# file = open('feat_color.data','w')
# pickle.dump(feat_color,file)
# file.close()
# file = open('colors.data','w')
# pickle.dump(colors,file)
# file.close()
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(dataTrain, labelTrain)
from sklearn.externals import joblib
# joblib.dump(clf, 'model.pkl', compress=9)
joblib.dump(clf, 'model2.pkl', compress=9)
