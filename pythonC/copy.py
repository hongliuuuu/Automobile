import numpy as np
import os
import re


def getkey(item):
    return item[5]

def overlap_area_xyhw(obj1, obj2):
   x1 = max(int(obj1[2]), int(obj2[2]));
   x2 = min(int(obj1[2]) + int(obj1[4]), int(obj2[2]) + int(obj2[4]));
   y1 = max(int(obj1[1]), int(obj2[1]));
   y2 = min(int(obj1[1]) + int(obj1[3]), int(obj2[1]) + int(obj2[3]));
   if (x1<x2 and y1<y2):
    return float((x2-x1+1)*(y2-y1+1))/(int((obj1[4]))*(int(obj1[3]))+(int(obj2[4]))*(int(obj2[3]))-(x2-x1+1)*(y2-y1+1))
   else:
    return 0
#l, t , w, h, score

def nms(frame_bb):
    output=[]
    f=frame_bb[0][0]
    if len(frame_bb)>1:
        i=0
        for bb in frame_bb:
            i=0
            for cc in frame_bb:

                l_frame=len(frame_bb)
                OL=overlap_area_xyhw(bb,cc)

                if OL>0.:
                    i=i+1
            if i==1:
                frame_bb.remove(bb)
        for bb in frame_bb:
            l_out=len(output)
            if l_out>0:
                for cc in output:
                    if bb[5]>cc[5]:
                        output.remove(cc)
                        output.append(bb)
            else:
                output.append(bb)


    #if(len(output)==0):
     #   output=[[f,' ',' ',' ',' ',' ']]
    #print(l_frame)
    return output
def frame_result(detection):
     frame_bb=[]
     all_bb=[]
     output=[]
     current_frame=0
     for item in detection:
         f=int(item[0])


         if(f>current_frame):
            if len(frame_bb)>0:
                output=nms(frame_bb)
                all_bb.append(output)
            current_frame=f
            frame_bb=[]
         frame_bb.append(item)
     output=nms(frame_bb)

     all_bb.append(output)
     return all_bb
        #frame=sorted(frame,key=getkey)
        #frame.sort(reverse=True)
#ll=[[1,384,90,64,64,1.23],[1,380,90,64,64,1.23],[1,384,95,64,64,2.23],[1,384,20,64,64,1.3]]
directory='./DropoutNew'


for root, dirs, files in os.walk("./dropout2"):
    for file in files:
          path = os.path.join(root, file)
          name,set,seq=[int(s) for s in re.findall(r'\d+', path)]
          npath=directory+('/set%02d' %set)
          if not os.path.exists(npath):
                os.makedirs(npath)
          nfile=npath+('/V%03d.txt'%seq)
          file = open(nfile,'w')
          f = open('./dropout2/set%02d/V%03d.txt'%(set,seq), 'r')


          x = f.readlines()
          for i in range(len(x)):
            x[i]=x[i].split()
          last=[]

          last=frame_result(x)

          for item in last:
              if(len(item)>0):
                print>>file, item[0][0],item[0][1],item[0][2],item[0][3],item[0][4],item[0][5]
          file.close()




