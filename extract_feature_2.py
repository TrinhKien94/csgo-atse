import csv


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


# testSet = load_data('test.csv')
testSet = load_data('test3.csv')
dataTest, labelTest = get_data_label(testSet)
from sklearn.naive_bayes import MultinomialNB
# clf = MultinomialNB()
# clf.fit(dataTrain, labelTrain)
from sklearn.externals import joblib
clf = joblib.load('model.pkl')
# test = []
# for i in range(0,10):
#     test.append(dataTest[i])
print dataTest[0]
y_predicted = clf.predict(dataTest)
lena = len(y_predicted)
dicti = {}
false_before = False
count_false = 0
count_true = 0
# f2 = open('training2.csv','w')
f2 = open('test2.csv','w')
for i in range(0,lena-1):
    dataLen = len(dataTest[i])
    text = str(labelTest[i])
    for j in range(0, dataLen):
        text += ',' + str(dataTest[i][j])
    if y_predicted[i+1] != labelTest[i+1]:
        text += ','+str(y_predicted[i+1])
        text += ',' + '0'
        # if false_before:
        #     count_false += 1
        # else:
        #     count_false = 1
        # false_before = True
    else:
        text += ',' + str(y_predicted[i+1])
        text += ',' + '1'
        # count_true += 1
        # if false_before:
        #     if count_false == 7:
        #         falses = []
        #         predicts = []
        #         for j in range(0,17):
        #             falses.append(labelTest[i-j])
        #             predicts.append(y_predicted[i-j])
        #         print 'falses:   '+str(falses)
        #         print 'predicts: '+ str(predicts)
        #     if count_false in dicti:
        #         dicti[count_false] += 1
        #     else:
        #         dicti[count_false] = 1
        # else:
        #     count_false = 0
        # false_before = False
    f2.write(text+'\n')
f2.close()
# print count_true
# f2 = open('predict_wrong_continues.txt','w')
# for key,value in dicti.items():
#     f2.write(str(key)+' '+str(value)+'\n')
# f2.close()
# from sklearn.metrics import accuracy_score
# print accuracy_score(labelTest, y_predicted)*100
# from sklearn.metrics import classification_report
# print(classification_report(labelTest, y_predicted))
# # # score = clf.score(dataTest, labelTest)
# # # print('Accuracy of sklearn: {0}%').format(score*100)
# # from sklearn.neighbors import KNeighborsClassifier
# # knn = KNeighborsClassifier()
# # knn.fit(dataTrain, labelTrain)
# # KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
# #            metric_params=None, n_jobs=1, n_neighbors=5, p=2,
# #            weights='uniform')
# # y_predicted = knn.predict(dataTest)
# # print accuracy_score(labelTest, y_predicted)
print 'total: '+str(lena)