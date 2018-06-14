from collections import OrderedDict
def convert_1_2(number):
    if number == '1':
        return '2'
    if number == '2':
        return '1'


def storeLog(log):
   hs = open("value.txt","a")
   hs.write(log+ "\n")
   hs.close()


def storeLog1950(log):
   hs = open("value1950.txt","a")
   hs.write(log+ "\n")
   hs.close()
# with open('test.txt') as f:
# with open('test2.txt') as f:
with open('data_normalized.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
sort_dict = OrderedDict()
count = len(content)-1
# contentNormalized = []
log = {}
for i in range(count,0,-1):
    datas = content[i].split('|')
    storeLog('|'.join(datas[0::2]))
    if int(datas[1]) == 195000:
        storeLog1950('|'.join(datas[0::2]))
        
#         if datas[1] in log:
#             log[datas[1]]+=1
#         else:
#             log[datas[1]]=1
# d_view = [ (v,k) for k,v in log.items() ]
# d_view.sort(reverse=True) # natively sort tuples by first element
# for v,k in d_view:
#     print("%s: %d" % (k,v))
