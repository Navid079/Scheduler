def avgTurnaroundTime(processes):
  sums = sum(process.getTurnaroundTime() for process in processes)
  avgs = sums / len(processes)
  return round(avgs, 3)

def avgWaitingTime(processes):
  sums = sum(process.getWaitingTime(None) for process in processes)
  avgs = sums / len(processes)
  return round(avgs, 3)

def avgResponseTime(processes):
  sums = sum(process.responseTime for process in processes)
  avgs = sums / len(processes)
  return round(avgs, 3)