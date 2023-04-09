import pyttsx3
import os
import playsound #for custom mp3 files

# Initialize text-to-speech engine
engine = pyttsx3.init()

def playGame(rounds, words, config): #TODO during rewrtiting rewrite this as well (rounds are neededonly for random)
    invalidStartingInput=True
    while invalidStartingInput:
        gameType=input("Linear [L] or Random [R]:")
        if gameType in ["L","l","Linear","linear"]:
            invalidStartingInput=False
            linearGame(words)

        elif gameType in ["R","r","Random","random"]:
            invalidStartingInput=False
            randomGame(words,rounds)
        

def linearGame(words):
    #starting point logic
    invalidStartingInput=True
    while invalidStartingInput:
        start=input("Start at (0 by default):")
        if len(start)==0:
            start=0
            invalidStartingInput=False
        else:
            try:
                start=int(start)
            except ValueError:
                for wordI,word in enumerate(words):
                    if word[0]==start:
                        start=wordI
                        invalidStartingInput=False
                        break
            else:
                if start<len(words):
                    invalidStartingInput=False

    #actually run the code
    for wordI in range(start,len(words)):
        while gameRound(words[wordI][0])=="r": #typing r will repeat the word
            pass

def randomGame(words,rounds):
    from random import randint
    for i in range(rounds):
        randI=randint(0,len(words)-1)
        while gameRound(words[randI][0])=="r":
            pass

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
    return input("Press Enter to continue...")