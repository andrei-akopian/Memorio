import pyttsx3
# import os
# import playsound #for custom mp3 files TODO add this

# Initialize text-to-speech engine
engine = pyttsx3.init()

def playGame(rounds, words, config):
    gameType=input("Linear [L] or Random [R]:")
    while True:
        if gameType in ["L","l","Linear","linear"]:
            linearGame(words)
            break
        elif gameType in ["R","r","Random","random"]:
            randomGame(rounds,words)
            break
        else:
            gameType=input("Reenter: Linear [L] or Random [R]:")

def randomGame(rounds,words):
    from random import randint
    correctCounter=0
    for i in range(rounds):
        randI=randint(0,len(words)-1)

        response=gameRound(words[randI][0])
        while response=="r":
            response=gameRound(words[randI][0])
        if response==words[randI][0]: #TODO add some percentage counters here
            correctCounter+=1
            print("Correct")
        else:
            print("Correct Spelling:",words[randI][0])
    print("Percentage Correct:",round(correctCounter/rounds,1))

def linearGame(words):
    #start at
    start=input("Start at (0 by default):")
    if len(start)==0:
        start=0
    elif len(start)<4:
        start=int(start) #TODO implement this using try/except
    else:
        for wordI,word in enumerate(words):
            if word[0]==start:
                start=wordI
                break
        if type(start)==str: #TODO create a while-loop until valid input
            print("Bad index") #And change this to something more understandable
            exit()

    for wordI in range(start,len(words)):
        response=gameRound(words[wordI][0])
        while response=="r":
            response=gameRound(words[wordI][0])
        if response==words[wordI][0]: #TODO add some percentage counters here
            print("Correct")
        else:
            print("Correct Spelling:",words[wordI][0])

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