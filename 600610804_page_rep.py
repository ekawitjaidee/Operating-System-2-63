import numpy as np
import matplotlib.pyplot as plt

def FIFO(rs,fsize):
  frame = []
  pf = 0
  for i in rs:
    if len(frame) < fsize:
      frame.append(i)
      pf += 1
    else:
      if i not in frame:
        frame.pop(0)
        frame.append(i)
        pf += 1
    # print(frame)
  return pf

def OPT(rs,fsize):
  frame = []
  pf = 0
  for i,st in enumerate(rs):
    if len(frame) < fsize: # if frame empty or less than framesize 
      frame.append(st)
      pf += 1
    else:                  # frame full
      if st not in frame:
        dist = []
        for j in frame:# find index of string in future 
          if j in rs[i:]:
            # print('rs = ',rs[i:])
            dist.append(rs[i:].index(j))
          else:
            dist.append(len(rs)+1)
        # print('dist = ',dist)
        frame.pop(np.argmax(dist))
        frame.insert(np.argmax(dist),st)
        pf += 1
    # print(frame)
  return pf

def LRU(rs,fsize):
  frame = []
  pf = 0
  for i,st in enumerate(rs):
    if len(frame) < fsize: # if frame empty or less than framesize 
      frame.append(st)
      pf += 1
    else:                  # frame full
      if st not in frame:
        dist = []
        for j in frame:# find index of string in past
          if j in rs[:i]:
            # print('rs = ',rs[:i])
            rrs = rs[:i]
            rrs.reverse()
            # print('rrs = ' ,rrs)
            dist.append(rrs.index(j))
          else:
            dist.append(-1)
        # print('dist = ',dist)
        frame.pop(np.argmax(dist))
        frame.insert(np.argmax(dist),st)
        pf += 1
    # print(frame)
  return pf

rs1 = [1,2,3,4,1,2,5,1,2,3,4,5]
rs2 = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
rs3 = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
# rs3 = [4, 8, 8, 3, 8, 5, 2, 6, 3, 0]
# print(FIFO(rs1,3))
# print(FIFO(rs1,4))
# print(FIFO(rs2,3))

# print(OPT(rs1,4))
# print(OPT(rs2,3))

# print(LRU(rs1,4))
# print(LRU(rs2,3))

#test case 
f = [3,4,5,6,7,8]
plist = []
for i in f:
  plist.append(FIFO(rs3,i))
  # print(OPT(rs3,i))
  # print(LRU(rs3,i))
print(plist)
plt.plot(f,plist)
plt.xlabel('Frame')
plt.ylabel('Page Fault')
plt.show()