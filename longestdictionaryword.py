#Astro Ohnuma
#12/6/17
#longestdictionaryword.py - finding the longest word in the dictionary

dictionary = open('engmix.txt')

wordcount = 0
for word in dictionary:
    m = ' '
    if len(word)>len(m):
        m = word
print('The longest word is',m)

