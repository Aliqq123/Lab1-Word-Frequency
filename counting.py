def countWords(words,stopWords):
    frequencies={}
    for word in words:
        if word in stopWords:
            continue
        elif word not in frequencies:
            frequencies[word]=1
        else:
            frequencies[word] +=1
    return frequencies



            