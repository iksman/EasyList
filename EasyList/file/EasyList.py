class ListCollection:
  def __init__(self):
    self.listItems = []

  def remove(self,item):
    newList = []
    for newitem in self.listItems:
      if newitem != item:
        newList += [newitem]
    self.listItems = newList

  def removeAll(self):
    self.listItems = []

  def add(self, listItem):
    if (type(listItem) == ListItem):
      self.listItems += [listItem]
      return True
    else:
      return False

  def toDict(self):
    items = []
    for item in self.listItems:
      items += [item.toDict()]
    return dict(listItems=items)

class ListItem:
  def __init__(self, title, description, priority, deadline, tasks = None):
    self.title = title
    self.description = description
    self.priority = priority
    self.deadline = deadline
    self.tasks = []
    if tasks != None:
      for task in tasks:
        self.addTask(task)

  def remove(self,task):
    newlist = []
    for item in self.tasks:
      if task != item:
        newlist += [item]
    self.tasks = newlist

  def removeAll(self):
    self.tasks = []
  
  def addTask(self, task):
    if (type(task) == Task):
      self.tasks += [task]
      return True
    else:
      return False

  def getTaskDict(self,dictToAppend):
    setDict = dictToAppend
    for task in self.tasks:
      setDict.get("tasks").append(task.toDict())
    return setDict

  def toDict(self):
    tempdict = dict(
        title=self.title,
        description=self.description,
        priority=self.priority,
        deadline=self.deadline,
        tasks=[]
    )
    return self.getTaskDict(tempdict)
    
    
     
class Task:
  def __init__(self, title, description, deadline):
    self.title = ""
    self.description = ""
    self.title = ""

    self.editTitle(title)
    self.editDesc(description)
    self.editDeadline(deadline)
    
  def editTitle(self, title):
    if (type(title) == str):
      self.title = title
      return True
    else:
      return False
  def editDesc(self, description):
    if (type(description) == str):
      self.description = description
      return True
    else:
      return False
  def editDeadline(self, deadline):
    if (type(deadline) == str):
      self.deadline = deadline
      return True
    else:
      return False

  def toDict(self):
    return dict(title=self.title,description=self.description,deadline=self.deadline)

#collection = ListCollection()
#collection.add(ListItem("EasyList","Small idea for a listmaker",1,"Nonexistent",[Task("Make a tasklist","None","AAA"),Task("Make another","None","AAB")]))
#collection.add(ListItem("EasyLister","Small idea for a listmakerer",12,"Nonexistenter",[Task("Make a tasklister","Noneer","AAAer"),Task("Make anotherer","Noneer","AABer")]))
#print(collection.toDict())


