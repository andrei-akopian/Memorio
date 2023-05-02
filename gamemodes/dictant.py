#Reads words alound, and you have to type them
import pyttsx3
import tools
# import os
# import playsound #for custom mp3 files TODO add this

# Initialize text-to-speech engine
engine = pyttsx3.init()

def playGame(rounds, words, config, clargs):
    _,mode=tools.selectionInput("Linear [L] or Random [R]:",clargs,modeInputChecker)
    #Linear
    if mode:
        _,start=tools.selectionInput("Start at (0 by default):",clargs,startInputChecker)
        linearGame(start,words)
    #Random
    else:
        randomGame(rounds,words)

def randomGame(rounds,words):
    from random import randint
    correctCounter=0
    for i in range(rounds):
        randI=randint(0,len(words)-1)

        response=gameRound(words[randI][0])
        while response=="r":
            response=gameRound(words[randI][0])
        if response==words[randI][0]: 
            correctCounter+=1 #TODO add familarity
            print("Correct")
        else:
            print("Correct Spelling:",words[randI][0])
    print("Percentage Correct:",str(round(correctCounter/rounds,1))+"%")

def linearGame(start,words):
    correctCounter=0
    for wordI in range(start,len(words)):
        response=gameRound(words[wordI][0])
        while response=="r":
            response=gameRound(words[wordI][0])
        if response==words[wordI][0]:
            correctCounter+=1
            #TODO add familarity
            print("Correct")
        else:
            print("Wrong, right spelling:",words[wordI][0])
    print("Percentage Correct:",str(round(correctCounter/rounds,1))+"%")

def gameRound(word):
    print(f"Word: {word}")
    #TODO implement the custom mp3 loading
    # mp3_file = os.path.join(".", f"mp3/{word}.mp3")
    # # Check if MP3 file exists
    # if os.path.exists(mp3_file):
    #     # Play the MP3 file
    #     playsound.playsound(mp3_file)
    # else:
    engine.say(word)
    engine.runAndWait()
    # Wait for user confirmation to proceed
    return input("Spell:")

#linear start check function for tools.selectionInput
def startInputChecker(start):
    """linear start check function for tools.selectionInput
    checks if inputed start for linear mode is valid, if yes, converts it into index
    """
    if len(start)==0: #if empty start at 0 by default
        return True, None
    elif start.isdigit():
        start=int(start)
        if 0<=start<len(words):
            return True, start
        else:
            return False, None
    else:
        for wordI,word in enumerate(words):
            if word[0]==start:
                start=wordI
                invalidStartingInput=False
                return True, wordI
        else:
            return False, None

#mode parsing check function for tools.selectionInput
def modeInputChecker(str_mode): #TODO add Linear as default
    """mode parsing check function for tools.selectionInput
    Encodes Linear as 1, and random as 0
    """
    if str_mode in "lLinear": #TODO there must be a better way to do this
        return True, 1
    elif str_mode in "rRandom":
        return True, 0
    else:
        return False, None