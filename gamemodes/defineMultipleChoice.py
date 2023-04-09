from random import randint

def randomSelector(words):
  total=0
  w=0
  for i,word in enumerate(words):
    total+=word[-1]
    if randint(0,total-1)<word[-1]:
      w=i
  return w

def randgen(words,n):
  l=[]
  while len(l)<n:
    w=randomSelector(words)
    if w not in l:
      l.append(w)
  return l

def revealWord(word):
  print("Correct Answer:")
  print("Word:",word[0])
  print("Defenition: ",word[1])
  print("Trivia: ", " ".join(word[2]))

def playGame(rounds, words,config):
  #load
  keymap=list(config["Settings"]["keymap"])

  correctCount = 0
  for roundN in range(rounds):
    print("#" * 20)
    print("Round:", roundN)
    result = gameRound(words,keymap)
    if result: 
      print("Correct")
    else: 
      print("Wrong")
    correctCount += result

  print("Score:", round(correctCount / rounds, 3) * 100, "%")

def gameRound(words,keymap):
  #question
  options = randgen(words,4)
  answer = randint(0,3)
  print("Define:", words[options[answer]][0])
  for i, option in enumerate(options):
    print(i, words[option][1])
  #answering
  response = input("G:")
  while type(response) == str:
    try:
      response = keymap.index(response)
    except:
      response = input("G:")
  if response == answer:
    words[options[answer]][-1]=abs(words[options[answer]][-1]-5) #TODO add better logic here
    return True
  else:
    words[options[answer]][-1]=abs(words[options[answer]][-1]+5)
    revealWord(words[options[answer]])
    return False