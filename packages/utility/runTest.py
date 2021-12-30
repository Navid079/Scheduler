from packages.utility.fileParser import parseFile, parseGanttFile
from packages.algorithms.fcfs import fcfs
from packages.algorithms.sjf import sjf
from packages.algorithms.srtn import srtn
from packages.algorithms.hrrn import hrrn
from packages.algorithms.rr import rr
from packages.algorithms.mlfq import mlfq

def runTest():
  print(f'FCFS')
  print('===========')
  for i in range(1, 5):
    processes, q1, q2 = parseFile(f'packages/test/inputs/test{i}.txt')
    expected = parseGanttFile(f'packages/test/fcfs/fcfs{i}.txt')
    got, avgTT, avgWT, avgRS = fcfs(processes)

    if str(expected) == str(got):
      print(f'Test#{i} passed')
    else:
      print(f'Test#{i} failed')
      print(f'Expected:\n{expected}')
      print(f'Got:\n{got}')

  print(f'\nSJF')
  print('===========')
  for i in range(1, 5):
    processes, q1, q2 = parseFile(f'packages/test/inputs/test{i}.txt')
    expected = parseGanttFile(f'packages/test/sjf/sjf{i}.txt')
    got, avgTT, avgWT, avgRS = sjf(processes)

    if str(expected) == str(got):
      print(f'Test#{i} passed')
    else:
      print(f'Test#{i} failed')
      print(f'Expected:\n{expected}')
      print(f'Got:\n{got}')

  print(f'\nSRTN')
  print('===========')
  for i in range(1, 5):
    processes, q1, q2 = parseFile(f'packages/test/inputs/test{i}.txt')
    expected = parseGanttFile(f'packages/test/srtn/srtn{i}.txt')
    got, avgTT, avgWT, avgRS = srtn(processes)

    if str(expected) == str(got):
      print(f'Test#{i} passed')
    else:
      print(f'Test#{i} failed')
      print(f'Expected:\n{expected}')
      print(f'Got:\n{got}')

  print(f'\nHRRN')
  print('===========')
  for i in range(1, 5):
    processes, q1, q2 = parseFile(f'packages/test/inputs/test{i}.txt')
    expected = parseGanttFile(f'packages/test/hrrn/hrrn{i}.txt')
    got, avgTT, avgWT, avgRS = hrrn(processes)

    if str(expected) == str(got):
      print(f'Test#{i} passed')
    else:
      print(f'Test#{i} failed')
      print(f'Expected:\n{expected}')
      print(f'Got:\n{got}')

  print(f'\nRR')
  print('===========')
  for i in range(1, 5):
    processes, q1, q2 = parseFile(f'packages/test/inputs/test{i}.txt')
    expected = parseGanttFile(f'packages/test/rr/rr{i}.txt')
    got, avgTT, avgWT, avgRS = rr(processes, q1)

    if str(expected) == str(got):
      print(f'Test#{i} passed')
    else:
      print(f'Test#{i} failed')
      print(f'Expected:\n{expected}')
      print(f'Got:\n{got}')

  print(f'\nMLFQ')
  print('===========')
  for i in range(1, 5):
    processes, q1, q2 = parseFile(f'packages/test/inputs/test{i}.txt')
    expected = parseGanttFile(f'packages/test/mlfq/mlfq{i}.txt')
    got, avgTT, avgWT, avgRS = mlfq(processes, q1, q2)

    if str(expected) == str(got):
      print(f'Test#{i} passed')
    else:
      print(f'Test#{i} failed')
      print(f'Expected:\n{expected}')
      print(f'Got:\n{got}')
  print('\n')