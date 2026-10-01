# definierar funktionen. frequencies = en dictionary {ord: antal}, n = hur många ord som ska skrivas ut
def printTopMost(frequencies, n):

    items = frequencies.items()
        # gör om dictionaryn till en sekvens av par, t.ex. ("the", 42)

    sorted_items = sorted(items, key=lambda pair: -pair[1])
    # sorterar paren och returnerar en ny lista
    # key=lambda: pair[0] är ordet, pair[1] är antalet
    # minustecknet gör att det största antalet hamnar först (fallande ordning)
    top_items = sorted_items[:n]
    # tar de n första paren i listan, alltså de n vanligaste orden


    for word, count in top_items:
    # loopar igenom varje par och delar upp det i word (ordet) och count (antalet)

        word_column = word.ljust(20)
        # fyller ut ordet med mellanslag till 20 tecken, vänsterjusterat
        count_column = str(count).rjust(5)
        # gör om antalet till text och högerjusterar det i 5 tecken
        print(word_column + count_column)
        # skriver ut ordet och antalet på samma rad så att kolumnerna hamnar under varandra
        
