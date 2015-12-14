#!/usr/bin/env python3

def word_count(phrase):
    words = phrase.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count
