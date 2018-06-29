from collections import OrderedDict
def convert_color(color):
    if color == 'red':
        return '2'
    if color == 'black':
        return '1'
    if color == 'green':
        return '0'

def convert_1_2(number):
    if number == '1':
        return '2'
    if number == '2':
        return '1'
# with open('test.txt') as f:
# with open('test2.txt') as f:
with open('predict.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
count = len(content)-1
# contentNormalized = []
y_predict = []
y_test = []
lose=[0] * 31
countLose = 0
for i in range(count,0,-1):
    datas = content[i].split('.0 ')
    if len(datas) == 2:
        y_predict.append(datas[0])
        y_test.append(datas[1])
        datas[0] = convert_1_2(datas[0])
        if countLose == 8 or countLose == 7:
            datas[0] = convert_1_2(datas[0])
        if countLose == 9:
            datas[0] = convert_1_2(datas[0])
        if datas[0] != datas[1]:
            countLose+=1
        else:
            lose[countLose]+=1
            countLose=0
from sklearn.metrics import accuracy_score
percent = 100*accuracy_score(y_test, y_predict)
print("Accuracy %.2f %%" %percent)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_predict))
print(lose)
for i in range(0,len(lose)):
    if lose[i]!=0:
        print(str(i)+" "+str(lose[i]))