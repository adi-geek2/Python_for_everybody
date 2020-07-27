fname = input("Enter file name: ")
fh = open(fname)
words = list()
word_list = list()
for line in fh:
    line.rstrip()
    words = line.split()
    for word in words:
        if word in word_list : continue
        word_list.append(word)
word_list.sort()
print(word_list) 