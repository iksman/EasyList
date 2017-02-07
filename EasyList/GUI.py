import Writer, json, Decoder
from EasyList import ListCollection, ListItem, Task

writer = Writer.Writer()

if not writer.firstTime:
  collection = Decoder.decodeDict(json.loads(writer.contents))
  print(collection.listItems[0].title)
  
writer.closeFile()