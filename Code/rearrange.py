import random, sys


def rearrange(words):
    '''Takes in a list of words and rearranges them into a new list'''
    # Lazy way
    # random.shuffle(list)
    # return list
    shuffle = []
    while len(words) != 0:
        word = random.choice(words)
        shuffle.append(word)
        words.remove(word)
    return(' '.join(shuffle))

if __name__ == "__main__":
    args = sys.argv[1:]
    shuffled = rearrange(args)
    print(shuffled)
