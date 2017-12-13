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
dictionary = open('engmix.txt')
for word in dictionary:
    word = word.strip()
    if word != '':
        if word[0] == 'r':
            print(word.strip())
