import random, sys


#Reads the file containing words and saves as a list
def get_lines(file):
    '''Opens a file and saves the lines in a new list without them ending
    in newlines.
    '''
    with open(file, "r") as f:
        dict_lines = f.readlines()
        lines_stripped = [word.strip() for word in dict_lines]
    return lines_stripped

def choose_words():
    '''Randomly chooses words from the list of words; The amount is based off of
    system argument amount. Then formats it to remove blankspaces.
    '''
    lines = get_lines("/usr/share/dict/words")
    word_list = []
    for _ in range(amount):
        word_list.append(random.choice(lines))
    return(' '.join(word_list))

if __name__ == "__main__":
    amount = int(sys.argv[1])
    print(choose_words())
