import csv
from numpy import genfromtxt
import numpy as np

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

def append_2d_array(arrayAppend,array2d):
    for element in array2d:
        arrayAppend.append(element)



# testSet = load_data('test.csv')
trainingSet = load_data('training.txt')
testSet = load_data('testing.txt')
X_train, y_train = get_data_label(trainingSet)
X_test, y_test = get_data_label(testSet)
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(dataTest, labelTest, test_size=0.33)
# from sklearn.naive_bayes import MultinomialNB
# clf = MultinomialNB()
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)
# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=15, p=2,weights='uniform')
# knn.fit(X_train, y_train)
# from sklearn.externals import joblib
# joblib.dump(knn, 'model-coinflip.pkl')
# y_pred = knn.predict(X_test)
# Load scikit's random forest classifier library



# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# from sklearn.neighbors import KNeighborsClassifier
# print(len(X_train))
# maxP = 0
# index = 0
# folkSize = 100
# X_train_combine = []
# y_train_combine = []
# indexs = []
# countModel = 0
# clfs=[]
# for i in range(0,len(X_train),folkSize):
#     end = i+folkSize-1
#     X_train_folk = X_train[i:end]
#     y_train_folk = y_train[i:end]
#     # clf = RandomForestClassifier(n_jobs=4, random_state=0,max_depth = 10,max_features =9, min_samples_split= 10,warm_start=True)
#     clf = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=15, p=2,weights='uniform')
#     clf.fit(X_train_folk, y_train_folk)
#     y_pred = clf.predict(X_test)
#     percent = 100*accuracy_score(y_test, y_pred)
#     if percent > 50.15:
#         clfs.append(clf)
#         from sklearn.externals import joblib
#         joblib.dump(clf, 'models/model-coinflip-'+str(countModel)+'.pkl')
#         countModel+=1
#     # if percent > 54.15:
#     #     append_2d_array(X_train_combine,X_train_folk)
#     #     append_2d_array(y_train_combine,y_train_folk)
#     #     indexs.append(i)
#     if percent > maxP:
#         maxP = percent
#         index = i
#     print("Accuracy of fold "+str(i)+": %.2f %%" %percent)
# print("Max Percent: "+str(maxP)+" at index: "+str(index))
# print(indexs)
# y_preds = []
# for i in range(0,len(clfs)):
#     y_preds.append(clfs[i].predict(X_test))
# print(len(y_preds))
# y_pred = []
# for j in range(0,len(y_preds[0])):
#     count_1 = 0
#     count_2 = 0
#     for i in range(0,len(y_preds)):
#         if y_preds[i][j] == 1.0:
#             count_1+=1
#         if y_preds[i][j] == 2.0:
#             count_2+=1
#     if count_2 > count_1:
#         y_pred.append(2.0)
#     else:
#         y_pred.append(1.0)
# print(y_pred)
# print(y_test)
# percent = 100*accuracy_score(y_test, y_pred)
# print("Accuracy of all %.2f %%" %percent)
# from sklearn.metrics import classification_report
# print(classification_report(y_test, y_pred))


# clf = RandomForestClassifier(n_jobs=2, random_state=0)
# clf = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=15, p=2,weights='uniform')
# clf.fit(X_train_combine, y_train_combine)
# y_pred = clf.predict(X_test)
# percent = 100*accuracy_score(y_test, y_pred)
# print("Accuracy of combine %.2f %%" %percent)
# print(len(X_train_combine))
# from sklearn.externals import joblib
# joblib.dump(clf, 'model-coinflip.pkl')
# clf = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=15, p=2,weights='uniform')
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)
# percent = 100*accuracy_score(y_test, y_pred)
# print("Accuracy of all %.2f %%" %percent)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier
clf = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=15, p=2,weights='uniform')
# clf = RandomForestClassifier(n_jobs=4, random_state=0,max_depth = 10,max_features =10, min_samples_split= 4000,warm_start=True)
# clf = MultinomialNB()
# clf = MLPClassifier(hidden_layer_sizes=(15,), random_state=1, max_iter=1, warm_start=True)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
from sklearn.metrics import accuracy_score
print("Accuracy of NB: %.2f %%" %(100*accuracy_score(y_test, y_pred)))
from sklearn.externals import joblib
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
joblib.dump(clf, 'model-coinflip.pkl')
loseLog = [0]*100
count = 0
for i in range(0,len(y_test)):
    if y_test[i]!=y_pred[i] and (y_pred[i]==1.0 or y_pred[i]==2.0):
        count+=1
    if y_test[i]==y_pred[i] and (y_pred[i]==1.0 or y_pred[i]==2.0):
        loseLog[count]+=1
        count = 0
print(loseLog)
bet = 10
maxBalance = 0
minBalance = 0
balance = 0
for i in range(0,len(y_test)):
    choice = float(np.random.random_integers(1,2))
    if y_test[i] != choice:
        balance -= bet
        if balance < minBalance:
            minBalance=balance
    else:
        balance +=bet*0.95
        if balance > maxBalance:
            maxBalance=balance

print("balance: "+str(balance))
print("minBalance: "+str(minBalance))
print("maxBalance: "+str(maxBalance))
