def read_file_words(file):
    with open(file, "r") as f:
        words = f.read().split()
    words = [word.lower() for word in words]
    return words

def histogram_list(file):
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
        print(histogram)
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
    '''Uses histogram data and returns the total count of unique words.'''
    return len(histogram)

def frequency(word, histogram):
    '''Returns the amount of times a word was seen from a given histogram data set.
    Works with list of lists or tuples.
    '''
    for list in histogram:
        if list[0] == word:
            return list[1]

def frequency_dict(word, histogram):
    '''Returns the amount of times a word was seen from a given histogram data set.
    Works with dictionary.
    '''
    for key, value in histogram.items():
        if key == word:
            return value


if __name__ == "__main__":
    histogram_list = histogram_list('textdocs/test.txt')
    unique_words = unique_words(histogram_list)
    word = 'go'
    word_frequency = frequency(word, histogram_list)

    print(histogram_list)
    print(f'Unique Words: {unique_words}')
    print(f'The amount of times the word "{word}" appeared in the text was: {word_frequency}')

    histogram_dict = (histogram_dict('textdocs/test.txt'))
    word_frequency_dict = frequency_dict(word, histogram_dict)
    print(histogram_dict)
    print(word_frequency_dict)

    # histogram_tuple = histogram_tuple('textdocs/test.txt')
    # print(histogram_tuple)
