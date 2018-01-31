#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import re
from collections import Counter, defaultdict


pat_hashes = re.compile('[#|:\-]+')
def is_valid_word(w):
    if w == '':
        return False
    if pat_hashes.match(w):
        return False
    return True


pat_sep = re.compile('[\"\s\(\)]+')
def split_words(line):
    words = pat_sep.split(line)
    return [w.lower() for w in words if is_valid_word(w)]


def get_words(filename):
    with open(filename, 'r') as f:
        for line in f:
            for w in split_words(line.strip()):
                if is_valid_word(w):
                    yield w.lower()

def first_of(limit, seq):
    i = 0
    while i < limit:
        yield next(seq)
        i += 1


def select_next_word(choices):
    all_options = [
        item 
        for k in choices.keys()
        for item in [k] * choices[k]
        ]
    return random.choice(all_options)


if __name__ == "__main__":
    
    counter = Counter()
    counter.update(get_words('prologo.md'))

    prev_word = None
    kernel = defaultdict(lambda: defaultdict(int))
    for word in get_words('prologo.md'):
        if prev_word:
            kernel[prev_word][word] += 1
        prev_word = word

    prev_word = None
    for word in get_words('estatutos.md'):
        if prev_word:
            kernel[prev_word][word] += 1
        prev_word = word

    start_words = list(kernel.keys())
    word = random.choice(start_words)
    for i in range(100):
        print(word, end=' ')
        word = select_next_word(kernel[word])


