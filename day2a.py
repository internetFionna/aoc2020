day2=open("day2.txt","r")
passDump=day2.read().split("\n")
day2.close()
validPass = 0
for i in range(len(passDump)-1):
    hyphenIndex=passDump[i].find("-")
    spaceIndex=passDump[i].find(" ")
    colonIndex=passDump[i].find(":")
    rangeStart=int(passDump[i][:hyphenIndex])
    rangeEnd=int(passDump[i][hyphenIndex+1:spaceIndex])
    findChar=passDump[i][colonIndex-1]
    charCount = passDump[i].count(findChar) - 1
    if charCount >= rangeStart and charCount <= rangeEnd:
        validPass += 1
print(validPass)
