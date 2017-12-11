#Astro Ohnuma
#12/11/17
#warmup16.py - Finding all the words in the dictionary that start with your first initial and end with your last initial

dictionary = open('engmix.txt')

for word in dictionary:
    word = word.strip()
    if word != '':
    if word[0] == 'a' and word[-1] == 'o':
        print(word.strip())