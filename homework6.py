#Astro Ohnuma
#12/7/17
#homework6.py - 6th computer science homework assignment

#1.
'''
dictionary = open('engmix.txt')
search = input('Enter a word to search for in the dictionary: ')
inside = False
for word in dictionary:
    if search == word.strip():
        inside = True
if inside == True:
    print(search,'is in the dictionary.')
elif inside == False:
    print(search,'is not in the dictionary.')
'''
#2.
'''
dictionary = open('engmix.txt')
words = []
for line in dictionary:
    words.append(line)
num = int(input('Enter a number: '))
print(words[num-1])
'''
#3.
dictionary = open('filedemo.py')
lines = []
for line in dictionary:
    lines.append(line.strip()+'!')
print(lines)
    