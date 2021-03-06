class Process:

  label = 'Px'
  startTime = 0
  burstTime = 0
  runTime = 0
  responseTime = -1
  endTime = -1

  def __init__(self, label, startTime, burstTime):
    self.label = label
    self.startTime = startTime
    self.burstTime = burstTime

  def __str__(self):
    return self.label

  def initialize(self):
    self.runTime = 0
    self.endTime = -1
    self.responseTime = -1

  def setStartTime(self, time):
    self.startTime = time
    self.initialize()

  def setBurstTime(self, time):
    self.burstTime = time
    self.initialize()

  def isFinished(self):
    return self.burstTime == self.runTime
  
  def stepInto(self, time):
    if self.responseTime < 0:
      self.responseTime = time - self.startTime
    self.runTime += 1

  def runTillEnd(self, time):
    if self.responseTime < 0:
      self.responseTime = time - self.startTime
    remainingTime = self.burstTime - self.runTime
    self.runTime = self.burstTime
    return remainingTime
  
  def finish(self, time):
    self.endTime = time
  
  def getWaitingTime(self, time):
    time = self.endTime if self.endTime > 0 else time
    return time - self.startTime - self.runTime
  
  def getTurnaroundTime(self):
    if self.endTime < 0: return -1
    return self.endTime - self.startTime
  
  def getRemainingTime(self):
    return self.burstTime - self.runTime
  
  def getResponseRatio(self, time):
    return 1 + (self.getWaitingTime(time) / self.burstTime)

  def stringify(self):
    return f'{self.label[1:]}, {self.startTime}, {self.burstTime}, {self.runTime}, {self.endTime}'