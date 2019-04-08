import csv
import pandas as pd

l = []
with open("ODI-2019-csv.csv","r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        l.append(row)

#print the number of records
print ("The number of records: %d" %(len(l) - 1))

str = ''
#print(l[0])#I don't know why there are two parts in this line???
print(str.join(l[0]).split(';'))

#print the number of attributes
number_of_attributes = len(str.join(l[0]).split(';'))
print ("The number of attributes: %d" %(number_of_attributes))


l_fixed = []
for item in l:
    str =''
    l_item = str.join(item).split(';')
    l_fixed.append(l_item)
del(l_fixed[0])

l_programme = []
for item in l_fixed:
    l_programme.append(item[1])

print (pd.value_counts(l_programme))

csv_file.close()
