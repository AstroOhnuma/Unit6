#Astro Ohnuma
#12/6/17
#longestdictionaryword.py - finding the longest word in the dictionary

dictionary = open('engmix.txt')

m = ' '
for word in dictionary:
    if len(word)>len(m):
        m = word
print('The longest word is',m)