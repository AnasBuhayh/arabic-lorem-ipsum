import pandas as pd
import random
import re

def generate_text(word_count=150):

    with open('data/raw_data.txt', encoding="utf8") as f:
        lines = f.readlines()
        lines = " ".join(lines)

    lines = lines.replace("\n", " ")
    split_lines = lines.split(".")
    random.shuffle(split_lines)

    sents = " ".join(split_lines) #combine all
    tokens = sents.split()
    print(len(tokens))
    words = tokens[:int(word_count)]
    lorem = " ".join(words)
    lorem = " ".join(lorem.split()) #remove white space

    while(lorem[-1] != " "): #revert to the last full word
        lorem = lorem[:-1]

    if len(lorem.split()[-1]) <= 4: #drop if a short word
        lorem = lorem.split()
        lorem.pop()
        lorem = " ".join(lorem)

    return lorem[:-1] + "."