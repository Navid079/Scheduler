class Burst:
  def __init__(self, process, startTime):
    self.process = process
    self.startTime = startTime
    self.length = 0
  
  def __str__(self):
    label = str(self.process) if self.process else 'H'
    return f'({self.startTime})[{label}]'
  
  def stepInto(self, time):
    if self.process: self.process.stepInto(time)
    self.length += 1

  def runTillEnd(self, time):
    time = self.process.runTillEnd(time) if self.process else 1
    self.length += time
    return time
  
  def stringify(self):
    process = self.process.stringify() if self.process else '-1, -1, -1, -1, -1'
    return f'{process}, {self.startTime}, {self.length}'