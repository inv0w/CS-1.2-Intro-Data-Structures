def read_file_words(file):
    with open(file, "r") as f:
        words = f.read().split()
    return words

def histogram(file):
    '''Reads a given text and counts the number of times a specific word
    was within the text. Returns a list of lists.
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

def histogram_dict(file):
    '''Reads a given text and counts the number of times a specific word
    was within the text. Returns a dictionary.
    '''
    text = read_file_words(file)
    histogram = {}
    for word in text:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def histogram_tuple(file):
    '''Reads a given text and counts the number of times a specific word
    was within the text. Returns a list of tuples
    '''
    text = read_file_words(file)
    histogram = []
    amount = 0
    for word in text:
        is_updated = False
        for tuple in histogram:
            if tuple[0] == word:
                amount = tuple[1] + 1
                histogram.remove(tuple)
                histogram.append((word, amount))
                is_updated = True
        if is_updated == False:
            histogram.append((word, 1))
    return histogram

def unique_words(histogram):
    '''Uses histogram data and returns the total count of unique words.
    Works with list of lists.
    '''
    word_counter = 0
    for list in histogram:
        word_counter += 1
    return word_counter

def frequency(word, histogram):
    '''Returns the amount of times a word was seen from a given histogram data
    set. Works with list of lists.
    '''
    for list in histogram:
        if list[0] == word:
            return list[1]

if __name__ == "__main__":
    histogram = histogram('textdocs/Sherlock.txt')
    unique_words = unique_words(histogram)
    word = 'mystery'
    word_frequency = frequency(word, histogram)

    print(histogram)
    print(f'Unique Words: {unique_words}')
    print(f'The amount of times the word "{word}" appeared in the text was: {word_frequency}')

    # histogram_dict = (histogram_dict('textdocs/test.txt'))
    # print(histogram_dict)
    #
    # histogram_tuple = histogram_tuple('textdocs/Sherlock.txt')
    # print(histogram_tuple)
