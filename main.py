from packages.utility.fileParser import parseFile, parseGanttFile
from packages.algorithms.fcfs import fcfs
from packages.algorithms.sjf import sjf
from packages.algorithms.srtn import srtn
from packages.algorithms.hrrn import hrrn

for i in range(1, 5):
  processes, q1, q2 = parseFile(f'packages/test/inputs/test{i}.txt')
  fcfs1 = parseGanttFile(f'packages/test/hrrn/hrrn{i}.txt')

  gantt = hrrn(processes)
  print('Expected:')
  print(fcfs1)
  print('Got:')
  print(gantt)
  print('==============================')