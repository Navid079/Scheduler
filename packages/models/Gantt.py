from .Burst import Burst

class Gantt:
  time = 0

  def __init__(self):
    self.bursts = []
  
  def addBurst(self, process):
    if self.getLastBurst().process is process:
      return
    self.bursts.append(Burst(process))

  def getLastBurst(self):
    if not self.bursts: return None
    return self.bursts[-1]

  def stepInto(self):
    self.getLastBurst().stepInto()
    self.time += 1
  
  def finishLastBurst(self):
    self.time += self.getLastBurst().runTillEnd()
    self.getLastBurst().process.finish(self.time)