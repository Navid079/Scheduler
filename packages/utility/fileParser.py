from ..models.Process import Process
from ..models.Burst import Burst
from ..models.Gantt import Gantt

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

def parseGanttFile(fileName):
  with open(fileName, 'r') as file:
    time = int(file.readline())
    burstStrings = file.readlines()
    burstStrings = [parseList(string) for string in burstStrings]
    bursts = []
    for string in burstStrings:
      label, startTime, burstTime, runTime, endTime, burstStartTime, burstLength = string
      process = Process(label, startTime, burstTime)
      process.runTime = runTime
      process.endTime = endTime
      burst = Burst(process)
      burst.startTime = burstStartTime
      burst.length = burstLength
      bursts.append(burst)
    gantt = Gantt()
    gantt.time = time
    gantt.bursts = bursts
    return gantt
def parseList(listString):
  listItem = listString.strip(',').strip(' ').strip(',').split(',')
  listItem = list(map(lambda item: int(item.strip(' ')), listItem))
  return listItem