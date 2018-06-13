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

def append_2d_array(arrayAppend,array2d):
    for element in array2d:
        arrayAppend.append(element)

# testSet = load_data('test.csv')
trainingSet = load_data('training.txt')
# testSet = load_data('testing.txt')
dataTest, labelTest = get_data_label(trainingSet)
# X_test, y_test = get_data_label(testSet)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dataTest, labelTest, test_size=0.3)
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
# for i in range(0,len(X_train),folkSize):
#     end = i+folkSize-1
#     X_train_folk = X_train[i:end]
#     y_train_folk = y_train[i:end]
#     clf = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=15, p=2,weights='uniform')
#     clf.fit(X_train_folk, y_train_folk)
#     y_pred = clf.predict(X_test)
#     percent = 100*accuracy_score(y_test, y_pred)
#     if percent > 54.15:
#         append_2d_array(X_train_combine,X_train_folk)
#         append_2d_array(y_train_combine,y_train_folk)
#         indexs.append(i)
#     if percent > maxP:
#         maxP = percent
#         index = i
#     print("Accuracy of fold "+str(i)+": %.2f %%" %percent)
# print("Max Percent: "+str(maxP)+" at index: "+str(index))
# print(indexs)
# # clf = RandomForestClassifier(n_jobs=2, random_state=0)
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
# clf = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=15, p=2,weights='uniform')
clf = RandomForestClassifier(n_jobs=4, random_state=0,max_depth = 10,max_features =9, min_samples_split= 10,warm_start=True)
# # from sklearn import svm
# # clf = svm.SVC()
# # clf.fit(X_train, y_train)
# # from sklearn import tree
# # clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
from sklearn.metrics import accuracy_score
print("Accuracy of NB: %.2f %%" %(100*accuracy_score(y_test, y_pred)))
from sklearn.externals import joblib
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
joblib.dump(clf, 'model-roulette.pkl')