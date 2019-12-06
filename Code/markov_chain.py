from .dictogram import Dictogram, read_file
import random


def higher_order_chain(word_list, new_words, order=2):
    '''Traverses through word_list and combines them into a string. How many words
    in the new string is based on the order number. If this string matches new_words
    add the new words to a list and combine it into a string.
    (Pair programmed with Anika Morris)

    word_list = str
    new_words = str
    order = int
    '''
    dicti = dict()
    key_words = new_words.split()
    words = []
    next_words = []
    next_pairs = []

    for i in range(len(word_list) - 1): #For each word in the word list
        words.clear()
        for j in range(order): #order is number from Markov Order
            if i < (len(word_list) - order): #Checks if following words would be outside the range of word_list
                words.append(word_list[i + j])
        if words == key_words: #If the words in the word list match our new words
            next_words.clear()
            for j in range(order): #Appends the next words and combines them into a string
                next_words.append(word_list[i + (j + 1)])
            next_words_str = ' '.join(next_words)
            next_pairs.append(next_words_str)

    dicti[new_words] = Dictogram(next_pairs)
    return dicti

def order_sample(word_list, order=2):
    '''Gets initial words from sampling to start higher_walk.

    word_list = str
    order = int
    '''
    next_words = []
    main_histogram = Dictogram(word_list)

    #Getting initial starting words
    next_word = main_histogram.sample()
    next_words.append(next_word)
    chain = next_chain(word_list, next_word)

    #Gets additional words based off the order
    for i in range(order - 1):
        if len(chain) > 0:
            following_word = chain.sample()
            next_words.append(following_word)
            chain = next_chain(word_list, following_word)

    sample = " ".join(next_words)
    return sample


def higher_walk(word_list, amount, order=2):
    '''First uses initial sample words to start the chain. Then uses the higher
    order chain to generate a full sentence using the order number. Amount will
    be the length of the sentence.

    word_list = str
    amount = int
    order = int
    '''
    sentence = []
    next_words = []

    #Initializing the starting sample words
    words_str = order_sample(word_list, order)
    sentence.append(words_str)
    next_words.append(words_str)

    #Generating the full sentence from amount number
    for i in range(amount - order):
        next_words.clear()
        chain = higher_order_chain(word_list, words_str, order)
        if len(chain[words_str]) > 0:
            words_str = chain[words_str].sample()
            next_words = words_str.split()
            sentence.append(next_words[order - 1])

    sentence = " ".join(sentence)
    return sentence


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


# def walk(word_list, amount):
#     '''Starts off the sentence with a sampled word from the initial histogram. Continues
#     to sample each new histogram to create a list of words.
#
#     word_list = list
#     amount = int
#     '''
#     sentence = []
#     main_histogram = Dictogram(word_list)
#     next_word = main_histogram.sample()
#     sentence.append(next_word)
#     for i in range((amount) - 1):
#         chain = next_chain(word_list, next_word)
#         if len(chain) > 0:
#             next_word = chain.sample()
#             sentence.append(next_word)
#
#     return sentence

def create_sentence(words):
    '''Joins words in a list, capitalizes the first word and adds a period
    to the end.

    words: list
    '''
    split_words = words.split()
    split_words[0] = split_words[0].capitalize()
    f_sentence = ' '.join(split_words) + '.'

    return f_sentence


if __name__ == '__main__':
    word_list = ['fish', 'two', 'fish', 'one', 'fish', 'two', 'fish', 'two', 'red', 'red', 'fish', 'blue', 'fish', 'cat']
    print(create_sentence(higher_walk(word_list, 15, 2)))
    # print(next_chain(word_list, 'fish'))
    # print(higher_order(word_list, 'fish two'))
    # print(higher_walk(word_list, 10))
    # print(order_sample(word_list, 2))
