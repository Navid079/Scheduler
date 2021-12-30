from packages.utility.fileParser import parseFile, parseGanttFile
from packages.algorithms.fcfs import fcfs

for i in range(1, 5):
  processes, q1, q2 = parseFile(f'packages/test/inputs/test{i}.txt')
  fcfs1 = parseGanttFile(f'packages/test/fcfs/fcfs{i}.txt')

  gantt = fcfs(processes)
  print('Expected:')
  print(fcfs1)
  print('Got:')
  print(gantt)
  print('==============================')