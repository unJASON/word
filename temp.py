import sys,re
from functools import reduce
import codecs
f = open('test.txt', 'rb')  # 源文本
line = f.readline()
array=line.decode('utf-8').split('][')
array[0] = array[0][1:]
print(array[0])
arraystr = array[0].split(', ')
array[-1] = array[-1][:-1]
print(array.__len__())
array = list(filter(lambda x : x.__len__()>3,array))
array = list(map(lambda x: x.split(', '),array))
f2 = codecs.open('shuju/test_after.txt', 'a', 'utf-8')
for i in range(array.__len__()):
    for j in range(array[i].__len__()):
        array[i][j] = array[i][j][1:-1]

for i in range(array.__len__()):
    for j in range(array[i].__len__()):
        f2.write(array[i][j])
        if i == array.__len__() -1 and j == array[i].__len__() - 1 :
            pass
        else:
            f2.write(" ")
f2.close()
f.close()