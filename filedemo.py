#Astro Ohnuma
#12/6/17
#filedemo.py - how to read a file

dictionary = open('engmix.txt')

wordcount = 0
for word in dictionary:
    if 'astro' in word:
        print(word.strip())
    wordcount += 1
    
print('There are', wordcount,'words in the dictionary.')

