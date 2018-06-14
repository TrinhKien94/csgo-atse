import csv
from numpy import genfromtxt


# Load data tu CSV file
def load_data(filename):
    lines = genfromtxt(filename, delimiter='|')
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [int(x) for x in dataset[i]]
    return lines

def get_data_label(dataset):
    data = []
    label = []
    for x in dataset:
        data.append(x[2::2])
        label.append(x[0])
    return data, label


testSet = load_data('testing.txt')
dataTest, labelTest = get_data_label(testSet)
from sklearn.externals import joblib
clfs = []
for i in range(0,88):
    clfs.append(joblib.load('models/model-coinflip-'+str(i)+'.pkl'))
y_preds = []
for i in range(0,len(clfs)):
    y_preds.append(clfs[i].predict(dataTest))
y_pred = []
y_test = []
for j in range(0,len(y_preds[0])):
    count_1 = 0
    count_2 = 0
    for i in range(0,len(y_preds)):
        if y_preds[i][j] == 1.0:
            count_1+=1
        if y_preds[i][j] == 2.0:
            count_2+=1
    total = count_1 + count_2
    percent_1 = float(count_1)/total
    percent_2 = float(count_2)/total
    if percent_1 > 0.6:
        y_test.append(labelTest[j])
        y_pred.append(1.0)
    if percent_2 > 0.6:
        y_test.append(labelTest[j])
        y_pred.append(2.0)
print(len(y_test))
print(len(y_pred))
from sklearn.metrics import accuracy_score
percent = 100*accuracy_score(y_test, y_pred)
print("Accuracy of all %.2f %%" %percent)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
# y_predicted = clf.predict(dataTest)
# lena = len(y_predicted)
# dicti = {}
# false_before = False
# count_false = 0
# count_true = 0
# print('total: '+str(len(y_predicted)))
# for i in range(0,lena):
#     if y_predicted[i] != labelTest[i]:
#         if false_before:
#             count_false += 1
#         else:
#             count_false = 1
#         false_before = True
#     else:
#         count_true += 1
#         if false_before:
#             if count_false == 7:
#                 falses = []
#                 predicts = []
#                 for j in range(0,17):
#                     falses.append(labelTest[i-j])
#                     predicts.append(y_predicted[i-j])
#                 print('falses:   '+str(falses))
#                 print('predicts: '+ str(predicts))
#             if count_false in dicti:
#                 dicti[count_false] += 1
#             else:
#                 dicti[count_false] = 1
#         else:
#             count_false = 0
#         false_before = False
# print(count_true)
# f2 = open('predict_wrong_continues2.txt','w')
# for key,value in dicti.items():
#     f2.write(str(key)+' '+str(value)+'\n')
# f2.close()
# from sklearn.metrics import accuracy_score
# print(accuracy_score(labelTest, y_predicted)*100)
# from sklearn.metrics import classification_report
# print(classification_report(labelTest, y_predicted))
# # score = clf.score(dataTest, labelTest)
# # print('Accuracy of sklearn: {0}%').format(score*100)
# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier()
# knn.fit(dataTrain, labelTrain)
# KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
#            metric_params=None, n_jobs=1, n_neighbors=5, p=2,
#            weights='uniform')
# y_predicted = knn.predict(dataTest)
# print accuracy_score(labelTest, y_predicted)
