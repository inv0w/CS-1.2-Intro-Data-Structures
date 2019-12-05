from dictogram import Dictogram, read_file
import random


def higher_order(word_list, new_words, order=2):
    ''''''
    dicti = dict()
    key_words = new_words.split()
    words = []
    next_words = []
    next_pairs = []

    for i in range(len(word_list) - 1): #For each word in the word list
        words.clear()
        for j in range(order): #n is number of Markov Order
            words.append(word_list[i + j]) #0 + 0 + 0 #0 + 0 + 1 (2)
        # print(words)
        if words == key_words: #If the words in the word list match our new words
            next_words.clear()
            for j in range(order):
                next_words.append(word_list[i + (j + 1)]) #0 + 0 + 1 #0 + 1 + 1 (2)
            next_words_str = ' '.join(next_words)
            next_pairs.append(next_words_str)

    dicti[new_words] = Dictogram(next_pairs)
    return dicti


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
    '''Starts off the sentence with a sampled word from the initial histogram. Continues
    to sample each new histogram to create a list of words.

    word_list = list
    amount = int
    '''
    sentence = []
    main_histogram = Dictogram(word_list)
    next_word = main_histogram.sample()
    sentence.append(next_word)
    for i in range((amount) - 1):
        chain = next_chain(word_list, next_word)
        if len(chain) > 0:
            next_word = chain.sample()
            sentence.append(next_word)

    return sentence

def create_sentence(words):
    '''Joins words in a list, capitalizes the first word and adds a period
    to the end.

    words: list
    '''
    words[0] = words[0].capitalize()
    f_sentence = ' '.join(words) + '.'

    return f_sentence


if __name__ == '__main__':
    word_list = ['fish', 'two', 'fish', 'one', 'fish', 'two', 'fish', 'two', 'red', 'red', 'fish', 'blue', 'fish', 'cat']
    # print(create_sentence(walk(word_list, 15)))
    print(higher_order(word_list, 'fish two'))
