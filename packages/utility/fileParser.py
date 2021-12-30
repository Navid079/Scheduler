from ..models.Process import Process

def parseFile(fileName):
  with open(fileName, 'r') as file:
    count = int(file.readline())
    labels = [f'P{i}' for i in range(count)]
    startTimes = file.readline()
    startTimes = parseList(startTimes)
    burstTimes = file.readline()
    burstTimes = parseList(burstTimes)
    q1 = int(file.readline())
    q2 = int(file.readline())
    processes = list(map(lambda data: Process(data[0], data[1], data[2]), zip(labels, startTimes, burstTimes)))
    return processes, q1, q2

def parseList(listString):
  listItem = listString.strip(',').strip(' ').strip(',').split(',')
  listItem = list(map(lambda item: int(item.strip(' ')), listItem))
  return listItem