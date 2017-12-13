#Astro Ohnuma
#12/13/17
#quiz6.py - quiz on files

# Program 1
dictionary = open('engmix.txt')
three = 'c'
two = 'p'
for word in dictionary:
    if word.count(three) == 3 and word.count(two) == 2:
        print(word.strip())
