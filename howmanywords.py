#Astro Ohnuma
#12/7/17
#howmanywords.py - prints out how many words there are for each number of letters in the dictionary

dictionary = open('engmix.txt')
words = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for word in dictionary:
    word = word.strip()
    words[len(word)-1] += 1
print('There are',words[0],'one letter words')
print('There are',words[1],'two letter words')
print('There are',words[2],'three letter words')
print('There are',words[3],'four letter words')
print('There are',words[4],'five letter words')
print('There are',words[5],'six letter words')
print('There are',words[6],'seven letter words')
print('There are',words[7],'eight letter words')
print('There are',words[8],'nine letter words')
print('There are',words[9],'ten letter words')
print('There are',words[10],'eleven letter words')
print('There are',words[11],'twelve letter words')
print('There are',words[12],'thirteen letter words')
print('There are',words[13],'fourteen letter words')
print('There are',words[14],'fifteen letter words')
print('There are',words[15],'sixteen letter words')
print('There are',words[16],'seventeen letter words')
print('There are',words[17],'eightteen letter words')
print('There are',words[18],'nineteen letter words')
print('There are',words[19],'twenty letter words')
print('There are',words[20],'twenty one letter words')
print('There are',words[21],'twenty two letter words')