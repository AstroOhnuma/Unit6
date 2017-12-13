#Astro Ohnuma
#12/13/17
#quiz6.py - quiz on files

# Program 1
'''
dictionary = open('engmix.txt')
three = 'c'
two = 'p'
for word in dictionary:
    if word.count(three) == 3 and word.count(two) == 2:
        print(word.strip())'''
# Program 2
'''
dictionary = open('engmix.txt')
words = []
for word in dictionary:
    word = word.strip()
    if word != '':
        if word[0] == 'r':
            words.append(word)
print(len(words))'''
# Program 3
'''
from random import randint
dictionary = open('engmix.txt')
num = int(input('Enter a number: '))
words = []
for word in dictionary:
    if num+1 == len(word):
        words.append(word)
print(words[randint(1,len(words))])'''
# Program 4
dictionary = open('engmix.txt')
letter = input('Enter a letter: ')
words = []
for word in dictionary:
    if letter not in word:
        words.append(word)
print(len(words))




