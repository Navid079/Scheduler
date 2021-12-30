def printOutput(processes, algorithm, label, q1 = 0, q2 = 0):
  print(label)
  print('==============')
  if q1 and q2:
    result, avgTT, avgWT, avgRT = algorithm(processes, q1, q2)
  elif q1:
    result, avgTT, avgWT, avgRT = algorithm(processes, q1)
  else:
    result, avgTT, avgWT, avgRT = algorithm(processes)
  print(result)
  print('Statistics:')
  print(f'Average Turnaround Time:\t{avgTT}')
  print(f'Average Waiting Time:\t\t{avgWT}')
  print(f'Average Response Time:\t\t{avgRT}')