import Writer, json, Decoder, GUI
from EasyList import ListCollection, ListItem, Task
writer = Writer.Writer()

if not writer.firstTime:
  collection = Decoder.decodeDict(json.loads(writer.contents))
  if collection != False:
    gui = GUI.GUI(collection,writer)