#External includes
#Main
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
#Read email addresses from the text
fh = open(fname)
count = 0
email_list = list()
for line in fh:
    line.rstrip()
    if not line.startswith('From'):continue
    wds = line.split()
    if len(wds) < 7 : continue
    print(wds[4])
    count += 1
print("There were", count, "lines in the file with From as the first word")
