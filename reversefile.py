#Astro Ohnuma
#12/7/17
#reversefile.py - asking the user for the name of a file and printing out all of the lines of the file in reverse order

flipped = input('Enter the name of a file: ')
file = open(flipped)
word = []
for line in file:
    word.append(line.strip())
word.reverse()
print(word)