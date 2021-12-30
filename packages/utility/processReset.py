def processReset(processes):
  for process in processes:
    process.initialize()
  processes.sort(key = lambda process: process.startTime)
  return processes