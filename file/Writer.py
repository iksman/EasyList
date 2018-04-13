import os.path, json, os
class Writer:
  def __init__(self):
    self.fileName = "list.json"
    if not self.checkExists():
      self.firstTime = True
      self.file = open(self.fileName,"w")
      self.file.close()
    else:
      self.firstTime = False
    self.file = open(self.fileName,"r+")
    self.contents = self.file.read()
      
  def closeFile(self):
    self.file.close()

  def saveOverwrite(self,dictionary):
    self.file.close()
    os.remove(self.fileName)
    self.file = open(self.fileName,"w")
    self.file.write(json.dumps(dictionary))


  def checkExists(self):
    if os.path.isfile(self.fileName):
      return True
    else:
      return False