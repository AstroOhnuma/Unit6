#Astro Ohnuma
#12/7/17
#homework6.py - 6th computer science homework assignment

dictionary = open('engmix.txt')
search = input('Enter a word to search for in the dictionary: ')
wordcount = 0
for word in dictionary:
    if search in word:
        inside = True
    else:
        inside = False
if inside == True:
    print(search,'is in the dictionary.')
elif inside == False:
    print(search,'is not in the dictionary.')

        
    