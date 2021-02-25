import numpy as np
import matplotlib.pyplot as plt
import random

def FIFO(rs,fsize): #get Refstring and Frame Size
  frame = [] #Frame
  pf = 0  # Page Fault Counting
  for i in rs:    #Loop Refstring
    if len(frame) < fsize: # if Frame empty or less than Frame Size / append page / counting page fault
      if i not in frame:
        frame.append(i)
        pf += 1
    else:                 # if Frame is Full / pop First page in Frame and append new page /counting page fault
      if i not in frame:
        frame.pop(0)
        frame.append(i)
        pf += 1

  return pf

def OPT(rs,fsize):
  frame = [] #Frame
  pf = 0  # Page Fault Counting
  for i,st in enumerate(rs):
    if len(frame) < fsize: # if Frame empty or less than Frame Size /  append page /counting page fault
      if st not in frame:
        frame.append(st)
        pf += 1
    else:                  # if Frame is Full
      if st not in frame:
        dist = []
        for j in frame:    # find index of string in future (left in Refstring)
          if j in rs[i:]:  # look in to future refstring
            dist.append(rs[i:].index(j))
          else:
            dist.append(len(rs)+1)

        frame.pop(np.argmax(dist))
        frame.insert(np.argmax(dist),st)
        pf += 1
    
  return pf

def LRU(rs,fsize):
  frame = [] #Frame
  pf = 0  # Page Fault Counting
  for i,st in enumerate(rs):
    dist = []
    if len(frame) < fsize: # if Frame empty or less than framesize / append page / couting page fault 
      if st not in frame:
        frame.append(st)
        pf += 1
    else:                  # if Frame full
      if st not in frame:
        for j in frame:    # find index of string in past
          if j in rs[:i]:  # look in to past Refstring
            rrs = rs[:i]
            rrs.reverse()
            dist.append(rrs.index(j))
          else:
            print(1)
            dist.append(len(rs)+1)
        maxindex = np.argmax(dist)
        frame.pop(maxindex)
        frame.insert(maxindex,st)
        pf += 1

  return pf


# test case
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


f = range(1,10)
fm = range(1,15)
random.seed(111)
# random.seed(112)
data1 = random.choices(f,k=50)
data2 = random.choices(f,k=60)
data3 = random.choices(f,k=70)
data4 = random.choices(f,k=80)
data5 = [1,2,3,4,4,3,2,1]*10
data6 = [1,2,3,4,1,2,5,1,2,3,4,5]*5
abc = data6
print(abc)
print(len(abc))
fifo,opt,lru = [],[],[]
for i in fm:
  fifo.append(FIFO(abc,i))
  opt.append(OPT(abc,i))
  lru.append(LRU(abc,i))

print(fifo,opt,lru)
plt.figure(figsize = (16,10))
plt.plot(fm,fifo)
plt.plot(fm,opt)
plt.plot(fm,lru)

plt.title('Data 6')
plt.grid()
plt.legend(['FIFO','OPT','LRU'])
plt.xlabel('Frame Number')
plt.ylabel('Page Fault')


plt.show()