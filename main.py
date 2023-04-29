import click
import configparser
import importlib #FIXME try to come up with a proper fix for this
import json
import banner

@click.group()
def commands():
  pass


#switching user
@click.command()
@click.option("--user", type=str, required=False, default=None)
@click.option("--keymap", type=str, required=False, default=None)
def configure(user,keymap):
  if user!=None:
    config["Settings"]["user"] = user
  if keymap!=None:
    config["Settings"]["keymap"] = keymap
  with open("config.ini", 'w') as f:
    config.write(f)


#new usre
@click.command("newuser")
@click.option("--user", type=str, default="default")
def newUserSetup(user):
  import json
  with open("vocabulary.json", "r") as f:
    data = json.load(f)
  with open(user + "_vocabulary.json", "w") as f:
    json.dump(data, f)
  print("Your files are set up, you are ready to go!")


#play
# @click.command("play")
# @click.option("-g","--gametype", default="None", type=str, required=False)
# @click.option("-v","--vocset", type=str, required=True) #FIXME rename vocset and Vocset
# @click.argument("rounds")
def game(gametype, vocset, rounds):
  if gametype == "None":
    print("you can play with all datasets or only certain ones")
  elif gametype in config["gamemodes"]:
    gameModule=importlib.import_module("gamemodes."+config["gamemodes"][gametype])
    gameModule.playGame(int(rounds), Vocsets[vocset]["data"], config) #TODO for future modes the entire vocset will be passed
    unloadVocsets(Vocsets)
  else:
    print("No such gamemode")

#coverter
@click.command("convocset",help="coverts CSV files into json")
@click.option("--name", default="test",type=str)
@click.argument("path")
def covertVocSet(name,path):
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

def loadVocsets(user):
  Vocsets={}
  with open(user + "_vocabulary.json", "r") as f:
    Vocsets = json.load(f)
  return Vocsets

def unloadVocsets(Vocsets):
  with open(config["Settings"]["user"] + "_vocabulary.json", "w") as f:
   json.dump(Vocsets,f)

@click.command("normal",help="just type this")
def normal():
  action=input("Action:")
  if action=="play":
    gametype=input("Gametype:")
    vocset=input("Vocset:")
    rounds=input("Rounds:")
    game(gametype,vocset,rounds)

commands.add_command(newUserSetup)
# commands.add_command(game)
commands.add_command(configure)
commands.add_command(covertVocSet)
commands.add_command(normal)

if __name__ == "__main__":
  config = configparser.ConfigParser()
  config.read("config.ini")

  #Load and display vocset and banner
  Vocsets=loadVocsets(config["Settings"]["user"])
  banner.displayBanner(Vocsets,config)

  commands()
