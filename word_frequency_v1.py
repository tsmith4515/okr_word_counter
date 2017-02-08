import string
import re
import pandas as pd

# Improvements:  (1) account for apostrophes or dashes in words,
#                (2) account for abbreviations (respons. for responsibility)
#                (3)

def word_frequency(txt_file):
    handle_capitals = input("""
    Would you like to count capitalized words as a
    separate word, or would you like me to make them all
    lowercase? Please enter 'y' or 'n'!\n""")
    print_list = input("""
    Ok, now would you like to print your list of words and
    their count to the console?  Please enter 'y' or 'n'.\n""")

    # word_frequency("example.txt", c)
    with open(txt_file) as f:
        content = f.readlines()
    # result will hold final dictionary of words with count associated
    result = {}

    # ADDITIONS
    # handling capitals
    if handle_capitals.lower() == 'y' or handle_capitals.lower() == 'yes':
        print("Got it! Capitals will be made lower-case. Here is your list.\n")
        content = [x.lower() for x in content]
    if handle_capitals.lower() == 'n' or handle_capitals.lower() == 'no':
        print("Okay, capitals will be considered separately.  See below.\n")

    # stripping of leading/tailing spaces and '\n' markers
    content = [x.strip() for x in content]

    # splitting each line into its words
    content = [x.split(' ') for x in content]

    # for loop to process each word and remove punctuation around it
    for line in content:
        for word in line:
            for c in string.punctuation:
                word = word.replace(c,"")

            # ADDITION BELOW
            # gets rid of quotations/spaces
            if word == "'" or word == "":
                continue
            if word in result:
                result[word] += 1
            elif word not in result:
                result[word] = 1

    if print_list.lower() == 'n' or print_list.lower() == 'no':
        None
    else:
        print("Total unique words in this file: \nAlphabetical Order (Word, Count)", len(result))
        for key in sorted(result):
            print("%s, %i" % (key, result[key]))

    return result

word_frequency('alice30.txt')
