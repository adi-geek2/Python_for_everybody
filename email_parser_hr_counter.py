#External includes
#Main
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
#Read email addresses from the text
fh = open(fname)
count = 0
hours_list = list()
hours_dist = dict()
hours_histogram = dict()
for line in fh:
    line.rstrip()
    if not line.startswith('From'):continue
    wds = line.split()
    if len(wds) < 7 : continue
    time = wds[5]
    time_sep = time.split(":")
    hours_list.append(time_sep[0]) 
for h in hours_list:
        hours_dist[h] = hours_dist.get(h,0) + 1    
hours_histogram = sorted(hours_dist.items())
for k,v in hours_histogram:
    print(k,v)
