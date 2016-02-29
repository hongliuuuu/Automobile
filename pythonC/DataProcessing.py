import numpy as np
import os

#def nms()



directory='./LFOV3OnlyN/set00/'
if not os.path.exists(directory):
    os.makedirs(directory)
f = open('./LFOV3Only/set00/V000.txt', 'r')
file = open('./LFOV3OnlyN/set00/V000.txt','w')

x = f.readlines()
for i in range(len(x)):
    x[i]=x[i].split()
last=[]
def getkey(item):
    return item[5]

def frame_result():

for i in range(int(x[len(x)-1][0])/30):
    frame=[]
    for s in x:
        if int(s[0]) == (i+1)*30:
            frame.append(s)
    if(len(frame)>1):
        frame=sorted(frame,key=getkey)
        frame.sort(reverse=True)
        last.append(frame[0])
        last.append(frame[1])
    else:
        last.append(frame[0])
for item in last:
    print>>file, item[0],item[1],

#file.close()




