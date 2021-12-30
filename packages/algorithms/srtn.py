from ..models.Gantt import Gantt
from ..utility.processReset import processReset


def srtn(processes):
  processes = processReset(processes)
  readyQueue = []
  gantt = Gantt()
  while processes or readyQueue:
    for process in processes:
      if process.startTime <= gantt.time: readyQueue.append(process)
    processes = list(filter(lambda process: process not in readyQueue, processes))
    process = min(readyQueue, key = lambda p: p.getRemainingTime())
    gantt.addBurst(process)
    gantt.stepInto()
    if process.isFinished():
      process.finish(gantt.time)
      readyQueue.remove(process)
  return gantt