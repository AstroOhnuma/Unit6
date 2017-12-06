#Astro Ohnuma
#12/6/17
#longestdictionaryword.py - finding the longest word in the dictionary

dictionary = open('engmix.txt')

wordcount = 0
for word in dictionary:
    longest = ''
    for w in word:
        if len(w)>len(longest):
            longest = word
print('The longest word is',longest)