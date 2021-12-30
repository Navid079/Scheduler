from ..models.Gantt import Gantt
from ..utility.processReset import processReset


def fcfs(processes):
  processes = processReset(processes)
  readyQueue = []
  gantt= Gantt()
  while processes and readyQueue:
    for process in processes:
      if process.startTime <= gantt.time: readyQueue.append(process)
    processes = list(filter(lambda process: process not in readyQueue, processes))
    process = readyQueue.pop(0)
    gantt.addBurst(process)
    gantt.finishLastBurst()
    readyQueue.remove(process)