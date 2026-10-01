
#skapar en funktion som heter tokenize med argumentet lines
def tokenize(lines):
    #skapar en lista som heter words
    words = []

    #en for loop som går genom varje rad i från inmatade argumentet lines
    for line in lines:
        #variabel start och end som kommer användas för att vi ska kunna navigera vart i meningen vi är.
        start = 0
        end = 0

        #en while loop som kommer köra så länge våran start variabel är mindre än antal strings i våran rad
        while start < len(line):
            #här vi döper våran nuvarande string(bokstav, tal, symbol) till i
            i = line[start]

            #en if sats där det checkar om våran i är en space, en bokstav eller en nummer, om det är ingen av de, då måste det vara en symbol
            if i.isspace():
                #som redan sagt start och end används för att navigera vart vi är i meningen. och här om det är en space då kommer det ba hoppa över det och inte spara det nånstans
                start = start+1

            elif i.isalpha():
                #om det är en bokstav kommer det spara det nuvarande start positionen av våran bokstav i end
                end = start

                #det kommer göra en while loop där det kommer checka om nästa string är också en bokstav så länge det är en bokstav det kommer fortsätta tills det träffar ingen bokstav,
                #samtidgt måste våran end(position) i raden vara mindre än antal postioner i raden så att vi inte försöker checka en string som inte finns
                while end < len(line) and line[end].isalpha():
                    end = end + 1

                #när vi träffar ingen mer bokstav kommer loopen att sluta köras, sen vi har våran start postion av det är ordet och end position och vi tar de och lägger till det ordet in i våran tumma words lista som vi skapade i början
                words.append(line[start:end])
                #sen vi sätter end = start så att loopen kan försätta köras från efter ordet är slut och inte behöve starta om innan bakom ordet
                start = end 

            #samma grejer som bokstav fast med nummer
            elif i.isdigit():
                end = start 

                while end < len(line) and line[end].isdigit():
                    end = end + 1
                words.append(line[start:end])
                start = end 
            #om det är en symbol det kommer bara lägga till den i våran lista direkt utan att behöva ha hansyn om nästa symbol är relaterad till den här eftersom symboler representeras alltid ensam
            else:
                words.append(line[start])
                start += 1   
    #när loopen är klar och vi har gått genom varje ord i varje mening i varje rad av den inmatade argument kommer vi gå genom varje element i words listan med en for loop och göra de till lower case, till exempel Apple blir apple
    words = [word.lower() for word in words]
    #sen det returnerar våran färdiga token lista words 
    return words
#puss


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


def printTopMost(frequencies, n):
  #Dict with frequency of word, word:freq, and how many words=n  
    items = frequencies.items()
#Makes dict to sequence, pair, (word:freq)
    
    sorted_items = sorted(items, key=lambda pair: -pair[1])
    #Sorting and returning new list, key makes it after freq
    #pair[0] word, pair[1]=n,-1 gives sorted falling
    top_items = sorted_items[:n]
    #from beginning t n , not n
    
    for word, count in top_items:
        #Lopp, word then count
        word_column = word.ljust(20)
        #20 tecken to the right
        count_column = str(count).rjust(5)
        #makes number to text, rjust string, to the left from right, 5 tecken
        print(word_column + count_column)
        #Makes it so word + counta
