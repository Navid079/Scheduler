import os
from packages.utility.fileParser import parseFile
from packages.algorithms.fcfs import fcfs
from packages.algorithms.sjf import sjf
from packages.algorithms.srtn import srtn
from packages.algorithms.hrrn import hrrn
from packages.algorithms.rr import rr
from packages.algorithms.mlfq import mlfq
from packages.utility.printOutput import printOutput
from packages.utility.runTest import runTest
from packages.utility.printManual import printManual

print('CPU Scheduler Simulator - V1.0.0')
print('By Navid')
print('Enter "manual" for help and instructions,')
print('"clear" to clear the screen,')
print('or "exit" to exit\n')
while True:
  fileName = input('Enter file name:(input.txt)> ')
  if fileName == 'exit':
    break
  if fileName == 'test':
    runTest()
  elif fileName == 'manual':
    printManual()
  elif fileName == 'clear':
    if os.name == 'posix':
      _ = os.system('clear')
    else:
      _ = os.system('cls')
  elif fileName:
    try:
      processes, q1, q2 = parseFile(fileName)
    except:
      print('No such file or directory')
      continue

    printOutput(processes, fcfs, 'First-Come-First-Served')
    printOutput(processes, sjf, 'Shortest-Job-First')
    printOutput(processes, srtn, 'Shortest-Remaining-Time-Next')
    printOutput(processes, hrrn, 'Highest-Response-Ratio-Next')
    printOutput(processes, rr, 'Round-Robin', q1)
    printOutput(processes, mlfq, 'MultiLevel-Feedback-Queue', q1, q2)
  else:
    processes, q1, q2 = parseFile('input.txt')

    printOutput(processes, fcfs, 'First-Come-First-Served')
    printOutput(processes, sjf, 'Shortest-Job-First')
    printOutput(processes, srtn, 'Shortest-Remaining-Time-Next')
    printOutput(processes, hrrn, 'Highest-Response-Ratio-Next')
    printOutput(processes, rr, 'Round-Robin', q1)
    printOutput(processes, mlfq, 'MultiLevel-Feedback-Queue', q1, q2)