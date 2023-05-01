import configparser
import importlib #FIXME try to come up with a proper fix for this
import json
import banner
import sys
import tools

#switching user
def configure(clargs):
  print("=Configuration=")
  target,_=tools.selectionInput("Target: ",clargs)
  value,_=selectionInput("Value: ",clargs)
  if target in config["Settings"]:
    config["Settings"][target]=value
  with open("config.ini", 'w') as f:
    config.write(f)

#new user
def newUserSetup(clargs):
  print("=New User setup=")
  vocsetName,_=tools.selectionInput("Newuser name:",clargs)
  import json
  with open("vocabulary.json", "r") as f:
    data = json.load(f)
  with open(user + "_vocabulary.json", "w") as f:
    json.dump(data, f)
  print("Your files are set up, you are ready to go!")

#play
def game(clargs):
  print("=Play Game=")#TODO add help&description here
  #inputs
  gametype,_=tools.selectionInput("Gametype: ",clargs,lambda gametype: (gametype in config["gamemodes"],None))
  vocset,_=tools.selectionInput("Vocset: ",clargs,lambda vocset: (vocset in Vocsets.keys(),None)) #the vocabulary set selection should probably be done differently
  _,rounds=tools.selectionInput("Rounds: ",clargs,lambda string: (string.isdigit(),int(string) if string.isdigit() else None))
  #load game
  gameModule=importlib.import_module("gamemodes."+config["gamemodes"][gametype])
  gameModule.playGame(rounds, Vocsets[vocset]["data"], config, clargs) #TODO for future modes the entire vocset will be passed
  #end
  unloadVocsets(Vocsets)

def covertVocSet(clargs): #TODO fix whatever nameing is going on here
  print("=Convert Vocset=")
  vocsetName=selectionInput("Vocset Name:",clargs)
  path=selectionInput("Path ot input file:",clargs)

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

def normal(clargs):
  action,_=tools.selectionInput("Action: ", clargs)

  if action=="play":
    game(clargs)
  elif action=="configure":
    configure(clargs)
  elif action=="convocset":
    covertVocSet(clargs)
  elif action=="newuser":
    newUserSetup(clargs)

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

  clargs=sys.argv
  #Load and display vocset and banner
  Vocsets=loadVocsets(config["Settings"]["user"])
  banner.displayBanner(Vocsets,config)

  normal(clargs[1:])
