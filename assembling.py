import sys
import urllib.request

from wordfreq import tokenize
from counting import countWords
from print_endresult import printTopMost

def read_text_lines(source):
    if source.startswitch("http://") or source.starswitch("https://"):
        response = urllib.request.urlopen(source)
        return response.read().decode("utf8").splitlines()
    else:
        with open(source, encoding="utf-8") as input-file:
            return input_file.readlines()

def read_stop_words(path):
    with open(path, encoding="utf-8") as input_file:
        return [line.strip() for line in input_file]

def main():
    stop_words_path = sys.argv[1]
    text_source = sys.argv[2]
    top_n = int(sys.argv[3])

    stop_words = read_stop_words(stop_words_path) 
    lines = read_text_lines(text_source)

    words = tokenize(lines)
    frequencies = countWords(words, stop_words)
    printTopMost(frequencies, top_n)  

main()     