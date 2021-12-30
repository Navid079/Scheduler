from packages.utility.fileParser import parseFile
from packages.algorithms.fcfs import fcfs
from packages.algorithms.sjf import sjf
from packages.algorithms.srtn import srtn
from packages.algorithms.hrrn import hrrn
from packages.algorithms.rr import rr
from packages.algorithms.mlfq import mlfq
from packages.utility.printOutput import printOutput
from packages.utility.runTest import runTest

fileName = input('Enter file name:(input.txt)\n')
if fileName == 'test':
  runTest()
elif fileName:
  processes, q1, q2 = parseFile(fileName)

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