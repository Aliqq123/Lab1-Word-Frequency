from countWords import countWords
from printTopMost import printTopMost


def tokenize(lines):
    words = []

    for line in lines:
        start = 0
        end = 0

        while start < len(line):
            i = line[start]

            if i.isspace():
                start = start+1

            elif i.isalpha():
                end = start

                while end < len(line) and line[end].isalpha():
                    end = end + 1
                words.append(line[start:end])
                start = end 
                
            elif i.isdigit():
                end = start 

                while end < len(line) and line[end].isdigit():
                    end = end + 1
                words.append(line[start:end])
                start = end 
            else:
                words.append(line[start])
                start += 1   

    words = [word.lower() for word in words]
    return words
