import numpy as np
import matplotlib.pyplot as plt
import random

def initial_process(pc_n,sec_1,sec_2):
  pc = []
  ps1 = round((pc_n/100)*sec_1)
  ps2 = ps1 + int((pc_n/100)*sec_2)

  for i in range(pc_n+1):
    try:
      if i == 0:
        continue
      elif i < ps1:
        pc.append((i,random.randint(2,8)))
      elif i < ps2:
        pc.append((i,random.randint(20,30)))
      else:
        pc.append((i,random.randint(35,40)))
    except:
      print('err at',i)
  print('process before shuffle : ',pc)
  random.shuffle(pc)
  print('process after shuffle : ',pc)
  return pc

def Fcfs(pc):
  waiting = 0
  wt = []
  print('Process  Waiting Time')
  for i in range(len(pc)):
    if i == 0 :
      print('  P'+str(pc[i][0])+'        ',0)
      wt.append(waiting)
      waiting+=pc[i][1]
    else:
      print('  P'+str(pc[i][0]),'       ',waiting)
      wt.append(waiting)
      waiting+=pc[i][1]
  print('-----------------------')
  print('Average = ',sum(wt)/len(pc))
  print('-----------------------')
  return wt
  
def Sjf(pc):
  waiting = 0
  wt = []
  pc.sort(key = lambda x: x[1])
  for i in range(len(pc)):
    if i == 0 :
      print('  P'+str(pc[i][0])+'        ',0)
      wt.append(waiting)
      waiting+=pc[i][1]
    else:
      print('  P'+str(pc[i][0]),'       ',waiting)
      wt.append(waiting)
      waiting+=pc[i][1]
  print('-----------------------')
  print('Average = ',sum(wt)/len(pc))
  print('-----------------------')
  return wt

def RR(pc, qt):
  wait = 0 
  flag = 0
  lpc=len(pc)
  wt = []
  while len(pc)>0:
    lst = []
    for i in range(len(pc)):
      if pc[i][1]>qt:
        lst.append((pc[i][0],pc[i][1]-qt))
        if flag ==0:
          print('  P'+str(pc[i][0])+'        ',0)
          flag=1
          wt.append(wait)
        else:
          print('  P'+str(pc[i][0]),'       ',wait)
          # wt.append(wait)
        wait+=qt
      else:
        if flag ==0:
          print('  P'+str(pc[i][0])+'        ',0)
          flag=1
          wt.append(wait)
        else:
          print('  P'+str(pc[i][0]),'       ',wait)
          wt.append(wait)
        wait+=pc[i][1]
    pc=lst
    
  print('-----------------------')
  print('Average = ',sum(wt)/lpc)
  print('-----------------------')
  return wt

def plot(pc,fcfs,sjf,rr,title):
  x = range(0,len(pc))
  plt.plot(x,fcfs,label="FCFS")
  plt.plot(x,sjf,label="SJF")
  plt.plot(x,rr,label="RR")
  plt.xlabel('Process Number')
  plt.ylabel('Burst Time')
  plt.title(title)
  plt.legend()
  plt.show()

random.seed(10001)
qt = 4 #quantum time for Round Robin algorithms

#initial Process
hypothesis1 = initial_process(60,70,20) #(Number of process, Percent of process bursttime in range (2,8),* in range(20,30))
hypothesis2 = initial_process(40,50,30)
hypothesis3 = initial_process(20,40,40)

#Hypythesis1
wt_fcfs = Fcfs(hypothesis1)
wt_sjf  = Sjf(hypothesis1)
wt_rr   = RR(hypothesis1,qt)
plot(hypothesis1,wt_fcfs,wt_sjf,wt_rr,'Hypothesis1')

#Hypythesis2
wt_fcfs = Fcfs(hypothesis2)
wt_sjf  = Sjf(hypothesis2)
wt_rr   = RR(hypothesis2,qt)
plot(hypothesis2,wt_fcfs,wt_sjf,wt_rr,'Hypothesis2')

#Hypythesis3
wt_fcfs = Fcfs(hypothesis3)
wt_sjf  = Sjf(hypothesis3)
wt_rr   = RR(hypothesis3,qt)
plot(hypothesis3,wt_fcfs,wt_sjf,wt_rr,'Hypothesis3')

