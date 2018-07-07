from collections import OrderedDict
class DataRoulette:
    id = 0
    color =''
    hash = ''
    lastMega = 0
    def __init__(self, id, color, hash, lastMega):
        self.id = id
        self.color = color
        self.hash = hash
        self.lastMega = lastMega
    def toString():
        return str(self.id) + "|" + self.color + "|" + self.hash + "|" + str(self.lastMega)
with open('roulette_data.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
sort_dict = OrderedDict()
for line in content:
    datas = line.split('|')
    sort_dict[datas[4]] = DataRoulette(int(datas[4]),datas[7],datas[5],datas[9])
    