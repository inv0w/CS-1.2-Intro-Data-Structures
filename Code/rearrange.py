import random, sys

def random_order(list):
    random.shuffle(list)
    return list

if __name__ == "__main__":
    words = sys.argv[1:]
    words_ran = random_order(words)
    print(' '.join(words_ran))
