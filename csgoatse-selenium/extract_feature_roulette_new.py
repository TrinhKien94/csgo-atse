stringSub = '0|0'
filename = 'roulette-data-test200.txt'
trainningSize = 90
# fileOut = '2-9.txt'
# def storeLog(log,f):
#    hs = open(f,"a")
#    hs.write(log+ "\n")
#    hs.close()

def getDataFromLine(line):
    line = line.replace('black','2')
    line = line.replace('green','0')
    line = line.replace('red','1')
    datas = line.split('|')
    # hashStr = []
    feature = []
    feature.append(datas[4])
    # for character in datas[5]:
    #     number = ord(character) - 96
    #     hashStr.append(number)
    # feature += hashStr
    feature.append(datas[6])
    # label = []
    # label.append(datas[8])
    label = datas[8]
    # label.append(datas[10])
    # feature.append(datas[10])
    feature = feature + datas[19::2]
    return label,feature

def readData(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    X_train = []
    y_train = []
    for line in content:
        label, features = getDataFromLine(line)
        X_train.append(features)
        y_train.append(label)
    return X_train, y_train
X_data, y_data = readData(filename)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier

lenData = len(X_data)
startIndex = 0
stopIndex = trainningSize
X_train = X_data[startIndex:stopIndex]
y_train = y_data[startIndex:stopIndex]
y_preds = []
y_tests = []
for i in range(trainningSize,lenData):
    clf = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=15, p=2,weights='uniform') 
    clf.fit(X_train,y_train)
    features = []
    features.append(X_data[i])
    y_preds.append(clf.predict(features)[0])
    y_tests.append(y_data[i])
    startIndex = startIndex + 1
    stopIndex = stopIndex + 1
    X_train = X_data[startIndex:stopIndex]
    y_train = y_data[startIndex:stopIndex]
# X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.33)
# clf = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=15, p=2,weights='uniform')
# # clf = RandomForestClassifier(n_jobs=4, random_state=0,max_depth = 10,max_features =70, min_samples_split= 10,warm_start=True)
# # clf = MultinomialNB()
# # clf = MLPClassifier(hidden_layer_sizes=(15,), random_state=1, max_iter=1, warm_start=True)
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)
from sklearn.metrics import accuracy_score
print("Accuracy of NB: %.2f %%" %(100*accuracy_score(y_tests, y_preds)))
from sklearn.externals import joblib
from sklearn.metrics import classification_report
print(classification_report(y_tests, y_preds))
joblib.dump(clf, 'model-roulette.pkl')
loseLog = [0]*100
count = 0
# print(y_tests)
for i in range(0,len(y_tests)):
    if y_tests[i]!=y_preds[i] and y_tests[i-6] == '0':
        count+=1
    if y_tests[i]==y_preds[i] and y_tests[i-6] == '0':
        loseLog[count]+=1
        count = 0
print(loseLog)