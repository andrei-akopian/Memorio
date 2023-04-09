import click
import configparser
import importlib #FIXME try to come up with a proper fix for this
import json

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
@click.command("play")
@click.option("-g","--gametype", default="None", type=str, required=False)
@click.option("-v","--vocset", type=str, required=True) #FIXME rename vocset and Vocset
@click.argument("rounds")
def game(gametype, rounds, vocset):
  if gametype == "None":
    print("you can play with all datasets or only certain ones")
  elif gametype in config["gamemodes"]:
    gameModule=importlib.import_module("gamemodes."+config["gamemodes"][gametype])
    Vocset=loadVocset(config["Settings"]["user"])
    gameModule.playGame(int(rounds), Vocset[vocset]["data"], config) #TODO for future modes the entire vocset will be passed
    unloadVocset(Vocset)
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

def loadVocset(user):
  Vocset={}
  with open(user + "_vocabulary.json", "r") as f:
    Vocset = json.load(f)
  return Vocset

def unloadVocset(Vocset):
  with open(config["Settings"]["user"] + "_vocabulary.json", "w") as f:
   json.dump(Vocset,f)

commands.add_command(newUserSetup)
commands.add_command(game)
commands.add_command(configure)
commands.add_command(covertVocSet)

if __name__ == "__main__":
  config = configparser.ConfigParser()
  config.read("config.ini")
  commands()
