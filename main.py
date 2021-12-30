from packages.utility.fileParser import parseFile, parseGanttFile
from packages.algorithms.fcfs import fcfs

processes, q1, q2 = parseFile('packages/test/test1.txt')
fcfs1 = parseGanttFile('packages/test/fcfs1.txt')

gantt = fcfs(processes)
print('Expected:')
print(fcfs1)
print('Got:')
print(gantt)