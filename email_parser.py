#External includes
#Main
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
#File handle
fh = open(fname)
email_counts = dict() 
email_list = list()
for line in fh:
    line.rstrip()
    if not line.startswith('From'):continue
    if len(line) < 40 : continue
    words = line.split()
    email_list.append(words[1])
for email in email_list :
    email_counts[email] = email_counts.get(email,0) + 1
highestCount = None
highestEmail = None    
for email,email_count in email_counts.items() :
    if highestCount is None or email_count > highestCount :
        highestCount = email_count
        highestEmail = email
print(highestEmail, highestCount)
