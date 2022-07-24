"""Generator function randomWord has as an argument list of words. It should return any random word from this list. Each time words are different until the end of the list is reached. Then words are taken from the initial list again.


For example if

list = ['book', 'apple', 'word']

books = randomWord(list)

then possible output example

first call of next(books) returns apple

second call of next(books) returns book

third call of next(books) returns word

fourth call of next(books) returns book
"""
import random


def randomWord(books):
    random.shuffle(books)
    for i in books:
        yield i
    if books:
        while True:
            yield random.choice(books)
    yield None


import collections

double_list = ["word1", "Biggg word", "last word"]
actual_list = []
random_element = randomWord(double_list)
for _ in range(len(double_list) * 2):
    actual_list.append(next(random_element))
print(collections.Counter(set(actual_list)) == collections.Counter(set(double_list * 2)))

import types

print(isinstance(randomWord([]), types.GeneratorType))

words = [3, 4, 7]
rand = randomWord([3, 2, 90])
list1 = []
list2 = []
for i in range(len(words)):
    list1.append(next(rand))
for i in range(len(words)):
    list2.append(next(rand))
print(list1 != list2)
