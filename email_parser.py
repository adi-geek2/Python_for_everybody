#External includes
#Main
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
<<<<<<< HEAD
#Read email addresses from the text
=======
#File handle
>>>>>>> 2d962938be7affe813e35c00dc4ef9d4d2d94563
fh = open(fname)
email_counts = dict() 
email_list = list()
for line in fh:
    line.rstrip()
    if not line.startswith('From'):continue
<<<<<<< HEAD
    wds = line.split()
    if len(wds) < 7 : continue
    print(wds[4])
    count += 1
print("There were", count, "lines in the file with From as the first word")
=======
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
>>>>>>> 2d962938be7affe813e35c00dc4ef9d4d2d94563
