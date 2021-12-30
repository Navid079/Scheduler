class Burst:
  def __init__(self, process, startTime):
    self.process = process
    self.startTime = startTime
    self.length = 0
  
  def __str__(self):
    return f'({self.startTime})[{str(self.process)}]'
  
  def stepInto(self, time):
    self.process.stepInto(time)
    self.length += 1

  def runTillEnd(self, time):
    time = self.process.runTillEnd(time)
    self.length += time
    return time
  
  def stringify(self):
    return f'{self.process.stringfy()}, {self.startTime}, {self.length}'