import sys

fp = open(sys.argv[1], 'r')

lines = fp.readlines()

txt = []

for i in lines:
    i = i.strip().lower().replace(',', '').replace('.', '').replace('?', '').replace('!', '').replace(':', '').replace(';', '')
    txt.append(i.split(' '))

word_count = 0

str = input("Enter the word to be searched: ")

for i in txt:
    word_count += i.count(str.lower())

print("The word", str, "occurs", word_count, "times in the file", sys.argv[1])
