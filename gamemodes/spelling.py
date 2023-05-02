# You are given the defenition and you have to spell the corresponding word
from random import randint

def playGame(rounds, words, config, clargs):
  correctCount = 0
  for roundN in range(rounds):
    print("#" * 20)
    print("Round:", roundN)
    result = gameRound()
    if result: 
      print("Correct")
    else: 
      print("Wrong")
    correctCount += result

  print("Score:", round(correctCount / rounds, 3) * 100, "%")

def revealWord(word):
  print("Correct Answer:")
  print("Word:",word[0])
  print("Defenition: ",word[1])
  print("Trivia: ", " ".join(word[2]))

def gameRound(words,keymap):
  #question
  secretWord=words[randint(0,len(words)-1)]
  print("Spell:", secretWord[1])
  #answering
  response = input("G:")
  if response=="H":
    print("Hint: ",secretWord[2])
    response = input("G:")
  if response==secretWord[0]:
    secretWord[-1]=abs(secretWord[-1]-5) #TODO add better logic here
    return True
  else:
    secretWord[-1]+=secretWord[-1]
    revealWord(secretWord)
    return False