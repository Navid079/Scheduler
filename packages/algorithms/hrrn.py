from ..models.Gantt import Gantt
from ..utility.processReset import processReset
from ..utility.statistics import avgTurnaroundTime, avgWaitingTime, avgResponseTime

def hrrn(processes):
  processes = processReset(processes)
  readyQueue = []
  backup = processes.copy()
  gantt = Gantt()
  while processes or readyQueue:
    for process in processes:
      if process.startTime <= gantt.time: readyQueue.append(process)
    processes = list(filter(lambda process: process not in readyQueue, processes))
    process = max(readyQueue, key = lambda p: p.getResponseRatio(gantt.time)) if readyQueue else None
    if process: readyQueue.remove(process)
    gantt.addBurst(process)
    gantt.finishLastBurst()
  return gantt, avgTurnaroundTime(backup), avgWaitingTime(backup), avgResponseTime(backup)