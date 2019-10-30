from analyze_words import read_file_words, histogram_dict
import sys
import random

def sample(histogram):
    ranindex = random.randint(0, len(histogram) - 1)
    keys = list(histogram.keys())
    return keys[ranindex]

def get_weight(histogram):
    pass

if __name__ == "__main__":
    arg = f'../Code/textdocs/{sys.argv[1]}'
    words = histogram_dict(arg)
    print(sample(words))
