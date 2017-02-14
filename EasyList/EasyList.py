import json
from file import Writer, Decoder, GUI
writer = Writer.Writer()

if not writer.firstTime:
  collection = Decoder.decodeDict(json.loads(writer.contents))
  if collection != False:
    gui = GUI.GUI(collection,writer)