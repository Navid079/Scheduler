class Burst:
  def __init__(self, process, startTime):
    self.process = process
    self.startTime = startTime
    self.length = 0
  
  def __str__(self):
    return f'({self.startTime})[{str(self.process)}]'
  
  def stepInto(self):
    self.process.stepInto()
    self.length += 1

  def runTillEnd(self):
    time = self.process.runTillEnd()
    self.length += time
    return time