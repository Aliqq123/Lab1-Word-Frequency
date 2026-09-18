test = "'They had 16 rolls of duct tape, 2 bags of clothes pins', '130 hampsters from the cancer labs down the hall, and', 'at least 500 pounds of grape jello and unknown amounts of chopped liver', 'said the source on a recent Geraldo interview.'"

def tokenize(document):
    document = document.split()

    for x in document:
        print(x)

tokenize(test)
