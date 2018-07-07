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
with open('log20160602-roulette.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
count = len(content)-1
fileNormalized = open("data_normalized_roulette.txt",'w')
for i in range(count,-1,-1):
    datas = content[i].split('|')
    if datas[0] == '0':
        datas[0] = '1'
    else:
        datas[0] = '0'
    content[i]='|'.join(datas)
for line in content:
    fileNormalized.write(line+'\n')
fileNormalized.close()
