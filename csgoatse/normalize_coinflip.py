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
with open('log20160602.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
sort_dict = OrderedDict()
count = len(content)-1
fileNormalized = open("data_normalized.txt",'w')
# contentNormalized = []
for i in range(count,-1,-1):
    datas = content[i].split('|')
    if datas[1].startswith('-'):
        number_convert = convert_1_2(datas[0])
        print("Line current: "+str(i+1)+" "+content[i])
        content[i]=number_convert+content[i][1:]
        print("Line fix: "+str(i+1)+" "+content[i])
    # datas = content[i].split('|')
    # content[i] = '|'.join(datas[0::2])
    # datas_prev = content[i-1].split('|')
    # if datas[2]!=datas_prev[0] and datas[3]==datas_prev[1]:
    #     print("Line fix: "+datas[2]+content[i-1][1:])
    #     print("Line current:"+content[i])
    #     print("Line prev:"+content[i-1])
    #     content[i-1]=datas[2]+content[i-1][1:]
for line in content:
    fileNormalized.write(line+'\n')
fileNormalized.close()
