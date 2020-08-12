#Numeral
import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_747709.txt"
#Read email addresses from the text
fh = open(fname)
count = 0
for line in fh:
    line.rstrip()
    numerals_in_line = re.findall('[0-9]+',line)
    if not numerals_in_line : continue
    for num in numerals_in_line :
        int_num = int(num)
        count += int_num
print(count)
        
    