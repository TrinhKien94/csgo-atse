with open('history.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
history = []
for line in content:
    round = int(line.split(' ')[0])
    history.append(round)
lenh = len(history)
for i in range(0,lenh-1):
    if history[i]+1 != history[i+1]:
        f = open('error-data.txt','a')
        f.write(str(history[i])+'\n')
        f.close()