
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
                end = start 

                while end < len(line) and not line[end].isdigit() and not line[end].isalpha() and not line[end].isspace():
                    end = end + 1
                words.append(line[start:end])
                start = end    

        words.low      
    return words



print(tokenize(['10  sweet  apple  tarts.']))