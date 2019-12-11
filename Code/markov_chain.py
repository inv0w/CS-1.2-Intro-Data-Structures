from .dictogram import Dictogram, read_file
import random


class Markov():
    '''Generates a sentence using a list of words using stochastic sampling
    to traverse through the list.

    word_list: list
    amount: int
    order: int
    '''

    def __init__(self, word_list, amount, order=2):
        """Initilize starting variables"""
        self.word_list = word_list
        self.amount = amount
        self.order = order

    def higher_order_chain(self, new_words):
        '''Traverses through word_list and combines them into a string. How many words
        in the new string is based on the order number. If this string matches new_words
        add the new words to a list and combine it into a string.
        (Pair programmed with Anika Morris)

        new_words: str
        '''
        dict_chain = dict()
        key_words = new_words.split()
        words = []
        next_words = []
        next_pairs = []

        for i in range(len(self.word_list) - 1): #For each word in the word list
            words.clear()
            for j in range(self.order): #order is number from Markov Order
                if i < (len(self.word_list) - self.order): #Checks if following words would be outside the range of word_list
                    words.append(self.word_list[i + j])
            if words == key_words: #If the words in the word list match our new words
                next_words.clear()
                for j in range(self.order): #Appends the next words and combines them into a string
                    next_words.append(self.word_list[i + (j + 1)])
                next_words_str = ' '.join(next_words)
                next_pairs.append(next_words_str)

        dict_chain[new_words] = Dictogram(next_pairs)
        return dict_chain

    def order_sample(self):
        '''Gets initial words from sampling to start higher_walk.'''
        next_words = []
        main_histogram = Dictogram(self.word_list)

        #Getting initial starting words
        next_word = main_histogram.sample()
        next_words.append(next_word)
        chain = self.next_chain(next_word)

        #Gets additional words based off the order
        for i in range(self.order - 1):
            if len(chain) > 0:
                following_word = chain.sample()
                next_words.append(following_word)
                chain = self.next_chain(following_word)

        sample = " ".join(next_words)
        return sample


    def higher_walk(self):
        '''First uses initial sample words to start the chain. Then uses the higher
        order chain to generate a full sentence using the order number. Amount will
        be the length of the sentence.
        '''
        sentence = []
        next_words = []

        #Initializing the starting sample words
        words_str = self.order_sample()
        sentence.append(words_str)

        #Generating the full sentence from amount number
        for i in range(self.amount - self.order):
            next_words.clear()
            chain = self.higher_order_chain(words_str) #Returns n order length of words
            if len(chain[words_str]) > 0:
                words_str = chain[words_str].sample()
                next_words = words_str.split()
                sentence.append(next_words[self.order - 1]) #Only get one item of next words to not repeat center word.

        sentence = " ".join(sentence)
        return sentence


    def next_chain(self, new_word):
        '''If a word is found and equals next_word, append the next word in the list.
        Then create a new histogram with the list of following words.

        new_word: str
        '''
        chain_list = []
        for i in range(len(self.word_list) - 1):
            if new_word == self.word_list[i]:
                chain_list.append(self.word_list[i + 1])

        chain = Dictogram(chain_list)
        return chain

    def create_sentence(self, words):
        '''Joins words in a list, capitalizes the first word and adds a period
        to the end.

        words: list
        '''
        split_words = words.split()
        split_words[0] = split_words[0].capitalize()
        f_sentence = ' '.join(split_words) + '.'

        return f_sentence

    def main(self):
        '''Combines all necessary functions to create a final sentence.'''
        words = self.higher_walk()
        sentence = self.create_sentence(words)
        return sentence


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


if __name__ == '__main__':
    word_list = ['fish', 'two', 'fish', 'one', 'fish', 'two', 'fish', 'two', 'red', 'red', 'fish', 'blue', 'fish', 'cat']
    markov = Markov(word_list, 15)
    print(markov.main())
