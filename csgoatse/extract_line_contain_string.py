stringSub = '0|0'
filename = 'training.txt'
fileOut = '0-0.txt'
def storeLog(log,f):
   hs = open(f,"a")
   hs.write(log+ "\n")
   hs.close()

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]
for line in content:
    if line.startswith(stringSub):
        datas = line.split('|')
        line_new = '|'+'|'.join(datas[0::2])+'|'
        storeLog(line_new,fileOut)    