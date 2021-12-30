from .Burst import Burst

class Gantt:
  time = 0

  def __init__(self):
    self.bursts = []
  
  def __str__(self):
    string = ''
    for burst in self.bursts:
      string += str(burst)
    string += f'({self.time})'
    return string
  
  def addBurst(self, process):
    if self.getLastBurst() and self.getLastBurst().process is process:
      return
    self.bursts.append(Burst(process, self.time))

  def getLastBurst(self):
    if not self.bursts: return None
    return self.bursts[-1]

  def stepInto(self):
    self.getLastBurst().stepInto(self.time)
    self.time += 1
  
  def finishLastBurst(self):
    self.time += self.getLastBurst().runTillEnd(self.time)
    if self.getLastBurst().process: self.getLastBurst().process.finish(self.time)

  def runQuantum(self, quantum):
    process = self.getLastBurst().process if self.getLastBurst() else None
    if process:
      for _ in range(quantum):
        if process.isFinished():
          return
        self.getLastBurst().stepInto(self.time)
        self.time += 1
    else:
      self.time += 1

  def saveToFile(self, fileName):
    with open(fileName, 'w') as file:
      file.write(f'{str(len(self.bursts))}\n')
      for burst in self.bursts:
        file.write(f'{burst.stringify()}\n')