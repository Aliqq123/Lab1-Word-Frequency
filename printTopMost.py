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
        #Makes it so word + count