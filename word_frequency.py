# input = Text file
# output = # of occurrences of every word
import string

def word_frequency(txt_file):
    with open(txt_file) as f:
        content = f.readlines()
    # result will hold final dictionary of words with count associated
    result = {}

    # stripping of leading/tailing spaces and '\n' markers
    content = [x.strip() for x in content]

    # splitting each line into its words
    content = [x.split(' ') for x in content]

    # for loop to process each word and remove punctuation around it
    for line in content:
        for word in line:
            for c in string.punctuation:
                word = word.replace(c,"")

            if word in result:
                result[word] += 1
            elif word not in result:
                result[word] = 1

    return result
