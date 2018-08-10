import collections
def convert_coin_to_number(coin):
    if coin == 'coin-ct':
        return '1'
    elif  coin == 'coin-t':
        return '2'
    elif  coin == 'coin-bonus':
        return '0'
    else:
        return '3'
with open('log.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
print('Read done')
history = {}
for line in content:
    coin, round, value = line.split(" ")
    coin = convert_coin_to_number(coin)
    round = int(round)
    history[round]=[coin,value]
print('Dict Done')
history = collections.OrderedDict(sorted(history.items()))
print('Sort done')
for k,v in history.items():
    f = open('history.txt','a')
    f.write(str(k)+' '+v[0]+' '+v[1]+'\n')
    f.close()