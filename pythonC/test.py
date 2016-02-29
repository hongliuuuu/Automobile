import os
import re

directory='./LFOV3OnlyNew'


for root, dirs, files in os.walk("./LFOV3Only"):
    for file in files:
          path = os.path.join(root, file)
          name,set,seq=[int(s) for s in re.findall(r'\d+', path)]
          npath=directory+('/set%02d' %set)
          if not os.path.exists(npath):
                os.makedirs(npath)
          nfile=npath+('/V%03d.txt'%seq)
          file = open(nfile,'w')

