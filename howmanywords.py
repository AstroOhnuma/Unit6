#Astro Ohnuma
#12/7/17
#howmanywords.py - prints out how many words there are for each number of letters in the dictionary

dictionary = open('engmix.txt')
words = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for word in dictionary:
    words[len(word)-1] = words[len(word)-1]+1
print(words)