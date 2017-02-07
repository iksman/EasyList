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

  def addTask(self, task):
    if (type(task) == Task):
      self.tasks += [task]
      return True
    else:
      return False
     
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

