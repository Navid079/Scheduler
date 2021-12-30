def printManual():
  with open('packages/manual/index.txt', 'r') as manual:
    for line in manual:
      print(line, end='')
  print('\n')