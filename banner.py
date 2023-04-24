def displayBanner(Vocsets): #TODO rename banner to something else
    import random
    with open("/Users/andrei/Documents/Coding/Projects/AnsiConverter/logoCompressed.txt") as f:
        logoRaw=f.readlines()

    logo=[]
    for logoRaw in logoRaw:
        cords=logoRaw.strip("\n").split(",")
        logo.append((int(cords[0]),int(cords[1])))

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

    while y<32:
        while x<32:
            if logo[pixelI]==(x,y):
                if len(word)==0:
                    if casefliper:
                        word=wordlist[random.randint(0,len(wordlist)-1)].upper()
                        casefliper=0
                    else:
                        casefliper=1
                        word=wordlist[random.randint(0,len(wordlist)-1)].lower()
                print(YELLOW+word[wordi],end="\033[0m")
                pixelI+=1
                if pixelI==len(logo):
                    print()
                    exit()
                wordi+=1
            else:
                if len(word)==0:
                    print(" ",end="")
                    casefliper=0
                else: 
                    print(BLACK+word[wordi],end="")
                    wordi+=1
            if wordi>=len(word):
                word=""
                wordi=0
            x+=1
        print(word[wordi:])
        word=""
        wordi=0
        x=0
        y+=1