from ..models.Gantt import Gantt
from ..utility.processReset import processReset

def rr(processes, quantum):
  processes = processReset(processes)
  readyQueue = []
  gantt = Gantt()
  process = None
  while processes or readyQueue or (process and not process.isFinished()):
    for p in processes:
      if p.startTime <= gantt.time: readyQueue.append(p)
    if process and not process.isFinished():
      readyQueue.append(process)
    processes = list(filter(lambda process: process not in readyQueue, processes))
    process = readyQueue.pop(0)
    gantt.addBurst(process)
    gantt.runQuantum(quantum)
    if process.isFinished():
      process.finish(gantt.time)
  return gantt