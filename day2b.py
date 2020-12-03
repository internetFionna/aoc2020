day2=open("day2.txt","r")
passDump=day2.read().split("\n")
day2.close()
validPass = 0
invalidPass = 0
for i in range(len(passDump)-1):
    hyphenIndex=passDump[i].find("-")
    spaceIndex=passDump[i].find(" ")
    colonIndex=passDump[i].find(":")
    pos1=int(passDump[i][:hyphenIndex])
    pos2=int(passDump[i][hyphenIndex+1:spaceIndex])
    findChar=passDump[i][colonIndex-1]
    charCount = passDump[i].count(findChar) - 1
    if findChar == passDump[i][colonIndex+pos1+1] and findChar == passDump[i][colonIndex+pos2+1]:
        invalidPass += 1
    elif findChar == passDump[i][colonIndex+pos1+1] or findChar == passDump[i][colonIndex+pos2+1]:
        validPass +=1
print(validPass)
