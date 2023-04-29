import configparser
import importlib #FIXME try to come up with a proper fix for this
import json
import banner
import sys

#switching user
def configure(target,value):
  if target in config["Settings"]:
    config["Settings"][target]=value
  with open("config.ini", 'w') as f:
    config.write(f)

#new user
def newUserSetup(user):
  import json
  with open("vocabulary.json", "r") as f:
    data = json.load(f)
  with open(user + "_vocabulary.json", "w") as f:
    json.dump(data, f)
  print("Your files are set up, you are ready to go!")

#play
def game(gametype, vocset, rounds):
  if gametype == "None":
    print("you can play with all datasets or only certain ones")
  elif gametype in config["gamemodes"]:
    gameModule=importlib.import_module("gamemodes."+config["gamemodes"][gametype])
    gameModule.playGame(int(rounds), Vocsets[vocset]["data"], config) #TODO for future modes the entire vocset will be passed
    unloadVocsets(Vocsets)
  else:
    print("No such gamemode")

def covertVocSet(name,path): #TODO fix whatever is going on here
  import csv
  oldData={}
  with open("vocabulary.json","r") as f:
    oldData=json.load(f)
  newDataRaw=[]
  with open(path,"r") as f:
    for line in csv.reader(f,delimiter=',',quotechar='"'):
      newDataRaw.append(line)
  
  oldData[name]={"structure":[newDataRaw[0][0],newDataRaw[0][1],newDataRaw[0][2:],"familarity"]}

  oldData[name]["data"]=[]
  for i in range(1,len(newDataRaw)):
    oldData[name]["data"].append([newDataRaw[i][0],newDataRaw[i][1],newDataRaw[i][2:],100])
  
  with open("vocabulary.json","w") as f:
    json.dump(oldData,f)

def normal():
  action=input("Action:") #TODO put all of these inputs into the actuall function
  if action=="play":
    gametype=input("Gametype:")
    vocset=input("Vocset:")
    rounds=input("Rounds:")
    game(gametype,vocset,rounds)
  elif action=="configure":
    target=input("Target:")
    value=input("Value:")
    configure(target, value)
  elif action=="convocset":
    vocsetName=input("Vocset Name:")
    path=input("Path ot input file:")
    covertVocSet(vocsetName,path)
  elif action=="newuser":
    vocsetName=input("Newuser name:")
    newUserSetup(vocsetName)

#Vocset loader&Unloader
def loadVocsets(user):
  Vocsets={}
  with open(user + "_vocabulary.json", "r") as f:
    Vocsets = json.load(f)
  return Vocsets

def unloadVocsets(Vocsets):
  with open(config["Settings"]["user"] + "_vocabulary.json", "w") as f:
   json.dump(Vocsets,f)

if __name__ == "__main__":
  config = configparser.ConfigParser()
  config.read("config.ini")

  #Load and display vocset and banner
  Vocsets=loadVocsets(config["Settings"]["user"])
  banner.displayBanner(Vocsets,config)

  normal()
