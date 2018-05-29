from collections import OrderedDict
def convert_color(color):
    if color == 'red':
        return '2'
    if color == 'black':
        return '1'
    if color == 'green':
        return '0'


# with open('test.txt') as f:
# with open('test2.txt') as f:
with open('27-05-2018.csv') as f:
    content = f.readlines()
content = [x.strip() for x in content]
sort_dict = OrderedDict()
count = len(content)-1
for line in content:
    elements = line.split(' ')
    print elements[1]
    # number = int(elements[0])
    number = count
    sort_dict[number] = {}
    # sort_dict[number]['color'] = elements[2]
    # print elements[0]
    sort_dict[number]['color'] = elements[0]
    # if len(elements)<3 and len(elements) > 0:
    #     sort_dict[number]['value'] = 0
    # else:
    sort_dict[number]['value'] = elements[1]
    count = count - 1
    # sort_dict[number] = elements[2]
reversed_sorted = OrderedDict(sorted(sort_dict.items(), reverse=True))
print reversed_sorted
keys = reversed_sorted.keys()
key_len = len(keys)
number_before = 9
extract_number_element_before = key_len - number_before
# data = open('test.csv','w')
# data = open('training.csv','w')
data = open('traning.csv','w')
for i in range(0,extract_number_element_before):
    text = convert_color(reversed_sorted[keys[i]]['color'])
    for j in range(i+1,i+number_before):
        # print reversed_sorted[keys[j]]['value']
        text = text + ',' + str(reversed_sorted[keys[j]]['value'])
    for j in range(i+1,i+number_before):
        text = text + ',' + convert_color(reversed_sorted[keys[j]]['color'])
    count = 1
    for j in range(i+2, i+11):
        if reversed_sorted[keys[i+1]]['color'] == reversed_sorted[keys[j]]['color']:
            count += 1
        else:
            break
    text += ',' + str(count)
    # len = 1
    # if reversed_sorted[keys[i+1]]['color'] != reversed_sorted[keys[i+len+1]]['color']:
    #     for k in range(2,len+1):
    #         if reversed_sorted[keys[i+k]]['color']== reversed_sorted[keys[i+1]]['color']:
    #             count+=1
    # if count == len-1:
    #     text = text + ',1'
    # # if count == 3:
    # #     text = text + ',1'
    # else:
    #     text = text + ',0'

    text = text + '\n'
    data.write(text)
data.close()
