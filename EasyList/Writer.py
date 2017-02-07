import os.path, json
class Writer:
  def __init__(self):
    if not self.checkExists():
      self.firstTime = True
      self.file = open("list.txt","w")
      self.file.close()
    else:
      self.firstTime = False
    self.file = open("list.txt","r+")
    self.contents = self.file.read()
      
  def closeFile(self):
    self.file.close()

  def saveOverwrite(self,dictionary):
    self.file.write(json.dumps(dictionary))



  def checkExists(self):
    if os.path.isfile("list.txt"):
      return True
    else:
      return False