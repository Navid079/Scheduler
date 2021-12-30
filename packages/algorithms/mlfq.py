from ..models.Gantt import Gantt
from ..utility.processReset import processReset
from ..utility.statistics import avgTurnaroundTime, avgWaitingTime, avgResponseTime

def mlfq(processes, quantum1, quantum2):
  processes = processReset(processes)
  backup = processes.copy()
  readyQueue1 = []
  readyQueue2 = []
  readyQueue3 = []
  gantt = Gantt()
  while processes or readyQueue1 or readyQueue2 or readyQueue3:
    for process in processes:
      if process.startTime <= gantt.time: readyQueue1.append(process)
    processes = list(filter(lambda process: process not in readyQueue1, processes))
    if readyQueue1:
      process = readyQueue1.pop(0)
      gantt.addBurst(process)
      gantt.runQuantum(quantum1)
      if process.isFinished():
        process.finish(gantt.time)
      else:
        readyQueue2.append(process)
    elif readyQueue2:
      process = readyQueue2.pop(0)
      gantt.addBurst(process)
      gantt.runQuantum(quantum2)
      if process.isFinished():
        process.finish(gantt.time)
      else:
        readyQueue3.append(process)
    elif readyQueue3:
      process = readyQueue3.pop(0)
      gantt.addBurst(process)
      gantt.finishLastBurst()
    else:
      gantt.addBurst(None)
      gantt.stepInto()
  return gantt, avgTurnaroundTime(backup), avgWaitingTime(backup), avgResponseTime(backup)