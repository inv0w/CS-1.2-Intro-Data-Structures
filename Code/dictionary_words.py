import random, sys

#This saves the command line argument as an integer
amount = int(sys.argv[1])

#Reads the file containing words and saves as a list
with open("/usr/share/dict/words", "r") as f:
    dict_lines = f.readlines()

def choose_words():
    '''Randomly chooses words from the list of words; The amount is based off of
    system argument amount. Then formats it to remove blankspaces.
    '''
    word_list = random.sample(dict_lines, amount)
    words_f = [w.strip() for w in word_list]
    return words_f


if __name__ == "__main__":
    print(' '.join(choose_words()))
