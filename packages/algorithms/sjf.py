from ..models.Gantt import Gantt
from ..utility.processReset import processReset
from ..utility.statistics import avgTurnaroundTime, avgWaitingTime, avgResponseTime

def sjf(processes):
  processes = processReset(processes)
  backup = processes.copy()
  readyQueue = []
  gantt = Gantt()
  while processes or readyQueue:
    for process in processes:
      if process.startTime <= gantt.time: readyQueue.append(process)
    processes = list(filter(lambda process: process not in readyQueue, processes))
    process = min(readyQueue, key = lambda p: p.burstTime)
    readyQueue.remove(process)
    gantt.addBurst(process)
    gantt.finishLastBurst()
  return gantt, avgTurnaroundTime(backup), avgWaitingTime(backup), avgResponseTime(backup)