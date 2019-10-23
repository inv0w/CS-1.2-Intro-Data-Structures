import random, sys

def reverse_word(list):
    '''Reverses the letters of words in a list'''
    reversed_list = [i[::-1] for i in list]
    return reversed_list

def reverse_sentence(list):
    '''Reverses all the words in a list'''
    return list[::-1]

if __name__ == "__main__":
    words = sys.argv[1:]
    words_r = reverse_word(words)
    sentence_r = reverse_sentence(words)
    print('Reversed words: ' + ' '.join(words_r))
    print('Reversed sentence: ' + ' '.join(sentence_r))
