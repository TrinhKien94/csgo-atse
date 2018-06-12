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


# testSet = load_data('test.csv')
trainingSet = load_data('training.txt')
testSet = load_data('testing.txt')
X_train, y_train = get_data_label(trainingSet)
X_test, y_test = get_data_label(trainingSet)
from sklearn.model_selection import train_test_split
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
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
from sklearn.metrics import accuracy_score
print("Accuracy of NB: %.2f %%" %(100*accuracy_score(y_test, y_pred)))
from sklearn.externals import joblib
joblib.dump(clf, 'model-coinflip.pkl')