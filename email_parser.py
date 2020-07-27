#External includes
#Main
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
email_list = list()
for line in fh:
    line.rstrip()
    if not line.startswith('From'):continue
    line = line.split()
    if len(line) < 7 : continue
    print(line[1])
    count += 1
print("There were", count, "lines in the file with From as the first word")
