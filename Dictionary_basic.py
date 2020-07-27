#Dictionary_basic
#Dictionary variables are key-value pair
#Order is not important
sample_dict = dict()
sample_dict['age'] = 21
sample_dict['name'] = "George"
print(sample_dict)
#Curly braces in output terminal indicates a dictionary
#Values are mutable
sample_dict['age'] = 23
print(sample_dict)
#Dictionaries can also be initialsed as curly braces
DCcomics = {}
DCcomics = {'Hero' : "Batman", 'Villian_1' : "Joker", 'Villian_2' : "Jester"}
print(DCcomics)
#Histograms with dictionaries
counts = dict()
names = ['csev','cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] += 1
print(counts)
#Get is a function that encapsulates above functionality