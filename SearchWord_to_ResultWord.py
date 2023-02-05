def findMinChars(searchWord,resultWord):
    x = 0
    y = 0
    # l = []
    while x != len(searchWord) and y!=len(resultWord):
        if searchWord[x] == resultWord[y]:
            # l.append(searchWord[x])
            x+=1
            y+=1
        else:
            x+=1
    # return len(resultWord)- len(l)
    return len(resultWord)- y
