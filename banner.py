#TODO add stats etc
def displayBanner(Vocsets,config): #TODO rename banner to something else
    #load in
    import random
    import os

    terminal_size = os.get_terminal_size() #TODO put this into main when rewritting
    bannertext=[]
    with open("logoPixels.txt","r") as f:
        logoRaw=f.readlines()
    with open("bannertext.txt","r") as f:
        bannertext=f.readlines()

    logo=[]
    for logoRaw in logoRaw:
        cords=logoRaw.strip("\n").split(",")
        logo.append((int(cords[0]),int(cords[1])))
    size=logo[0][:]
    del logo[0]

    YELLOW="\033[38;5;220m"
    BLACK="\033[38;5;240m"

    x=0
    y=0
    wordlist=[]
    for key in Vocsets.keys():
        i=0
        while len(wordlist)<100:
            wordlist.append(Vocsets[key]["data"][i][0])
            i+=1
        if len(wordlist)==100:
            break

    word=""
    wordi=0
    pixelI=0
    casefliper=0
    color=BLACK

    line=""
    banner=[]
    maxlen=0

    while y<size[1]:
        while x<size[0]:
            if logo[pixelI]==(x,y):
                if len(word)==0:
                    if casefliper:
                        word=wordlist[random.randint(0,len(wordlist)-1)].upper()
                        casefliper=0
                    else:
                        casefliper=1
                        word=wordlist[random.randint(0,len(wordlist)-1)].lower()
                if color==BLACK:
                    line+=YELLOW
                    color=YELLOW
                line+=word[wordi]
                pixelI+=1
                wordi+=1
            else:
                if color==YELLOW:
                    line+=BLACK
                    color=BLACK
                if len(word)==0:
                    line+=" "
                    casefliper=0
                else: 
                    line+=word[wordi]
                    wordi+=1
            if wordi>=len(word):
                word=""
                wordi=0
            x+=1
            if pixelI==len(logo):
                break

        if color==YELLOW:
            line+=BLACK
            color=BLACK
        line+=word[wordi:]
        #save the results
        maxlen=max(maxlen,size[0]+len(word)-wordi)
        banner.append([line,size[0]+len(word)-wordi])
        #reset for next cycle
        line=""
        word=""
        wordi=0
        x=0
        y+=1
        if pixelI==len(logo):
            break

    #TODO make the bannertext display the input variables from a generated list.
    for lineI in range(len(banner)):
        banner[lineI][0]+=" "*(maxlen-banner[lineI][1])+"\033[0m"
        print(banner[lineI][0],
            bannertext[lineI][:terminal_size[0]-maxlen-1].strip("\n").format(
                version=config["About"]["version"],
                user=config["Settings"]["user"],
                keymap=config["Settings"]["keymap"]))
    print()
    return banner