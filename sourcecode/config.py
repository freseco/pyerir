import json
import os
from pathlib import Path
class config():
    def __init__(self):
      self.file=os.path.join(Path( __file__ ).parent.absolute(),"config.json")
      self.data={"provider":{
                  "name":"",
                  "server" : "",
                  "username" : "",
                  "password" : ""
               },
               "IPTV_url":"",
               "m3u_file":""}
      #read json file
      self.readjson()
      
    def savejson(self):      
      with open(self.file, "w") as p:
         json.dump(self.data, p)
          
    def readjson(self):
      with open(self.file, "r") as read_it:
         self.data = json.load(read_it)
         #print(self.data)