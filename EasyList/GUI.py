import Writer, InpOptions, os
from EasyList import *

class InputHandler:
  def __init__(self,gui):
    self.gui = gui
  def inputHandler(self,function,parameter=None):
    inp = input("?>")
    isInt = self.gui.parse(inp)

    if inp.lower() in InpOptions.quit:
      self.gui.quit()
    
    elif (function == self.gui.main and 
          inp.lower().split(" ")[0] in InpOptions.item and 
          len(inp.split(" ")) > 1 and 
          self.gui.parse(inp.lower().split(" ")[1])):

      if int(inp.split(" ")[1]) <= len(self.gui.collection.listItems):
        os.system("cls")
        item = int(inp.lower().split(" ")[1])
        if item > 0:
          self.gui.specItem(self.gui.collection.listItems[item - 1])
    #END

    elif function == self.gui.specItem and inp.lower() in InpOptions.back:
      os.system("cls")
      self.gui.main()

    elif inp.lower() in InpOptions.add:
      if function == self.gui.main:
        self.addHandler(function)
      elif function == self.gui.specItem:
        self.addHandler(function, parameter)

    elif (function == self.gui.main and 
          inp.lower().split(" ")[0] in InpOptions.remove and 
          len(inp.split(" ")) > 1 and 
          self.gui.parse(inp.lower().split(" ")[1])):
      self.removeHandler(function,int(inp.lower().split(" ")[1]))

    elif (function == self.gui.main and 
          inp.lower().split(" ")[0] in InpOptions.remove and 
          len(inp.split(" ")) > 1 and 
          inp.lower().split(" ")[1] in InpOptions.allP):
      self.gui.collection.removeAll()

    elif (function == self.gui.specItem and 
          inp.lower().split(" ")[0] in InpOptions.remove and 
          len(inp.split(" ")) > 1 and 
          self.gui.parse(inp.lower().split(" ")[1])):
      self.removeHandler(function,int(inp.lower().split(" ")[1]),parameter)
    
    elif (function == self.gui.specItem and 
          inp.lower().split(" ")[0] in InpOptions.remove and 
          len(inp.split(" ")) > 1 and 
          inp.lower().split(" ")[1] in InpOptions.allP):
      parameter.removeAll()

    #elif inp.lower() in InpOptions.save:
      #self.gui.writer.saveOverwrite(self.gui.collection.toDict())
    
    os.system("cls")
    if parameter != None:#Lambda
      function(parameter)
    else:
      function()

  def addHandler(self, function,item=None):
    if function == self.gui.main:
      title = input("Title: ")
      description = input("Description: ")
      while True:
        priority = input("Priority: ")
        if self.gui.parse(priority):
          break
      deadline = input("Deadline: ")      
      self.gui.addItem(title,description,priority,deadline)
    if function == self.gui.specItem:
      title = input("Title: ")
      description = input("Description: ")
      deadline = input("Deadline: ")
      item.addTask(Task(title,description,deadline))

  def removeHandler(self, function, num, item=None):
    if function == self.gui.main:
      if len(self.gui.collection.listItems) >= int(num) and num > 0:
        self.gui.collection.remove(self.gui.collection.listItems[num - 1])
    elif function == self.gui.specItem:
      if len(item.tasks) >= int(num) and num > 0:
        item.remove(item.tasks[num - 1])

class GUI:
  def __init__(self,data,writer):
    self.collection = data
    self.writer = writer
    self.inputHandler = InputHandler(self)
    self.main()    

  def addItem(self,title,description,priority,deadline):
    self.collection.add(ListItem(title,description,priority,deadline))

  def main(self):
    print("--Iksman's EasyList--\n -Main Menu-\n")
    for item in self.collection.listItems:
      index = self.collection.listItems.index(item)
      print("Item " + str(index+1) + ":")
      print("\tTitle: "+ item.title)
      print("\tDescription: " + item.description)
      print("\tPriority: " + str(item.priority))
      print("\tDeadline: " + item.deadline)
      print("\tTasks: " + str(len(item.tasks)) + "\n")
    self.inputHandler.inputHandler(self.main)#Lambda here
    #self.quit()

  def specItem(self, item):
    print("--Iksman's EasyList--\n -Item View-\n")
    index = self.collection.listItems.index(item)
    print("Item " + str(index+1) + ":")
    print("\tTitle: "+ item.title)
    print("\tDescription: " + item.description)
    print("\tPriority: " + str(item.priority))
    print("\tDeadline: " + item.deadline + "\n")
    for newItem in item.tasks:
      newIndex = item.tasks.index(newItem)
      print("\tTask " + str(newIndex + 1) + ":")
      print("\t\tTitle: " + newItem.title)
      print("\t\tDescription: " + newItem.description)
      print("\t\tDeadline: " + newItem.deadline + "")
    self.inputHandler.inputHandler(self.specItem, item)  

  def parse(self, input):
    try:
      int(input)
      return True
    except:
      return False

  def quit(self):
    self.writer.saveOverwrite(self.collection.toDict())
    self.writer.closeFile()
    quit()


     