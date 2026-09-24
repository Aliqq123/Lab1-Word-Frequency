def printTopMost(frequencies, n):
    #Need to make dict to sequence, word, number
    #items will return key value couple in dict
    items = frequencies.items()

    #Sort pair, frequency, from -1
    sorted_items = sorted(items, key=lambda pair: -pair[1])
    #Only the first n, slicing :n, up to n
    top_items = sorted_items[:n]

    #Adjusted, nice, printing
    for word, count in top_items:
        #ljust to right, 20 tecken
        word_column = word.ljust(20)
        count_column = str(count).rjust(5)
        #str, nuber->text
        #rjust to lef , 5 tecken
        print(word_column + count_column)
        