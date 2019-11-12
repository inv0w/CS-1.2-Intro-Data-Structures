from dictogram import Dictogram, read_file
import random


def next_chain(word_list, new_word):
    '''If a word is found and equals next_word, append the next word in the list.
    Then create a new histogram with the list of following words.

    word_list = list
    new_word = str
    '''
    chain_list = []
    for i in range(len(word_list) - 1):
        if new_word == word_list[i]:
            chain_list.append(word_list[i + 1])

    chain = Dictogram(chain_list)
    return chain


def walk(word_list, amount):
    '''Starts off the sentence with a sampled word from initial histogram. Continues
    to sample each new histogram to create a list of words.

    word_list = list
    amount = int
    '''
    sentence = []
    main_histogram = Dictogram(word_list)
    next_word = main_histogram.sample()
    sentence.append(next_word)
    for i in range(amount):
        chain = next_chain(word_list, next_word)
        next_word = chain.sample()
        sentence.append(next_word)

    return sentence

def create_sentence(words):
    '''Joins words in a list and capitalizes the first word and adds a period
    to the end.

    words: list
    '''
    words[0] = words[0].capitalize()
    f_sentence = ' '.join(words) + '.'

    return f_sentence


if __name__ == '__main__':
    word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    print(create_sentence(walk(word_list, 15)))
