from analyze_words import read_file_words, histogram_dict
import sys
import random
import pytest

def sample(histogram):
    ranindex = random.randint(0, len(histogram) - 1)
    keys = list(histogram.keys())
    return keys[ranindex]

def sample_by_frequency(histogram):
    '''Takes in a dictionary histogram and adds the keys to a new list a certain
    amount of times based on their values

    histogram: Dictionary
    '''
    frequency_list = []
    for key, value in histogram.items():
        [frequency_list.append(key) for i in range(value)]
    ran_index = random.randint(0, len(frequency_list) - 1)
    return frequency_list[ran_index]

def test_sample_by_frequency():
    frequency_dict = {}
    words = histogram_dict('../Code/textdocs/test.txt')
    for i in range(100000):
        sample_word = sample_by_frequency(words)
        if sample_word in frequency_dict:
            frequency_dict[sample_word] += 1
        else:
            frequency_dict[sample_word] = 1

    return frequency_dict


if __name__ == "__main__":
    arg = f'../Code/textdocs/{sys.argv[1]}'
    words = histogram_dict(arg)
    print(sample_by_frequency(words))
    print(test_sample_by_frequency())
