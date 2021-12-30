class Burst:
  def __init__(self, process):
    self.process = process
    self.length = 0
  
  def stepInto(self):
    self.process.stepInto()
    self.length += 1

  def runTillEnd(self):
    time = self.process.runTillEnd()
    self.length += time
    return time