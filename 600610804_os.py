import numpy as np
import matplotlib.pyplot as plt
import random

def initial_process(pc_n,sec_1,sec_2):
  pc = []

  ps1 = round((pc_n/100)*sec_1)
  ps2 = ps1 + int((pc_n/100)*sec_2)


  for i in range(pc_n+1):
    try:
      if i ==0:
        continue
      elif i < ps1:
        pc.append((i,random.randint(2,8)))
      elif i < ps2:
        pc.append((i,random.randint(20,30)))
      else:
        pc.append((i,random.randint(35,40)))
    except:
      print('err at',i)

  random.shuffle(pc)
  return pc



def Fcfs(pc):
  waiting = 0
  print('Process | Waiting Time')
  for i in range(len(pc)):
    if i == 0 :
      print('  P'+str(pc[i][0])+'   |     ',0)
      waiting+=pc[i][1]
    else:
      print('  P'+str(pc[i][0]),'  |     ',waiting)
      waiting+=pc[i][1]
  print('-----------------------')
  print('Average = ',waiting/len(pc))
  
def Sjf(pc):
  waiting = 0
  pc.sort(key = lambda x: x[1])
  for i in range(len(pc)):
    if i == 0 :
      print('  P'+str(pc[i][0])+'   |     ',0)
      waiting+=pc[i][1]
    else:
      print('  P'+str(pc[i][0]),'  |     ',waiting)
      waiting+=pc[i][1]
  print('-----------------------')
  print('Average = ',waiting/len(pc))

def RR(pc, qt):
  wait = 0 
  flag = 0
  while len(pc)>0:
    lst = []
    for i in range(len(pc)):
      if pc[i][1]>qt:
        lst.append((pc[i][0],pc[i][1]-qt))
        if flag ==0:
          print('  P'+str(pc[i][0])+'   |     ',0)
          flag=1
        else:
          print('  P'+str(pc[i][0]),'  |     ',wait)
        wait+=qt
      else:
        if flag ==0:
          print('  P'+str(pc[i][0])+'   |     ',0)
          flag=1
        else:
          print('  P'+str(pc[i][0]),'  |     ',wait)
        wait+=pc[i][1]
    pc=lst
  return pc


x = initial_process(60,70,20)
test = [(1,6),(2,8),(3,7),(4,3)]
t = [(1,24),(2,3),(3,3)]
# Fcfs(test)
# Sjf(test)
RR(t,4)

