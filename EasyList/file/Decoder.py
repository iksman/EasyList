from file import EasyList

def decodeDict(dictionary): #Add exceptions
  collection = EasyList.ListCollection()
  try:
    for listItem in dictionary.get("listItems"):
      tasklist = []
      for tasks in listItem.get("tasks"):
        tasklist += [EasyList.Task(tasks.get("title"), tasks.get("description"), tasks.get("deadline"))]
      collection.add(EasyList.ListItem(listItem.get("title"),listItem.get("description"),listItem.get("priority"),listItem.get("deadline"),tasklist))
    return collection
  except:
    return False #if json is tempered with  
  