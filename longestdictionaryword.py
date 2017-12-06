#Astro Ohnuma
#12/6/17
#longestdictionaryword.py - finding the longest word in the dictionary

dictionary = open('engmix.txt')

wordcount = 0
for w in dictionary:
    m = ' '
    if len(w)>len(m):
        m = w
print('The longest word is',m)