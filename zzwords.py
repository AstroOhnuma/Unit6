#Astro Ohnuma
#12/7/17
#zzwords.py - print out all the words in the dictionary that contain "zz"

dictionary = open('engmix.txt')

for word in dictionary:
    if 'astro' in word:
        print(word.strip())


