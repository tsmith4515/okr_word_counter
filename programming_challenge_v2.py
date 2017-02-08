import string
import re
import pandas as pd

def prefix_counter(file, prefix):
    d = word_frequency('alice30.txt')
    prefix = prefix.lower()
    result = []
    for k,v in d.items():
        if prefix == k[0:len(prefix)]:
            print(k,v)

prefix_counter('alice30.txt', 'you')
