#Astro Ohnuma
#12/7/17
#homework6.py - 6th computer science homework assignment

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

        
    