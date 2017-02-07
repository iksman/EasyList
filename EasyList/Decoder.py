from EasyList import *
def decodeDict(dictionary): #Add exceptions
  collection = ListCollection()
  for listItem in dictionary.get("listItems"):
    tasklist = []
    for tasks in listItem.get("tasks"):
      tasklist += [Task(tasks.get("title"), tasks.get("description"), tasks.get("deadline"))]
    collection.add(ListItem(listItem.get("title"),listItem.get("description"),listItem.get("priority"),listItem.get("deadline"),tasklist))
  return collection
  