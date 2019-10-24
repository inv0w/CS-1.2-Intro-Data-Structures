def read_file_words(file):
    with open(file, "r") as f:
        words = f.read().split()
    return words

def histogram(file):
    '''Reads a given text and counts the number of times a specific word
    was within the text.
    '''
    text = read_file_words(file)
    histogram = []
    for word in text:
        is_updated = False
        for list in histogram:
            if list[0] == word:
                list[1] += 1
                is_updated = True
        if is_updated == False:
            histogram.append([word, 1])
    return histogram

def unique_words(histogram):
    '''Uses histogram data and returns the total count of unique words'''
    pass

def frequency():
    '''Returns the amount of times a word was seen from a given histogram data
    set.
    '''
    pass

if __name__ == "__main__":
    print(histogram('textdocs/test.txt'))
