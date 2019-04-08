import csv

l = []
with open("ODI-2019-csv.csv","r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        l.append(row)

#print the number of records
print (len(l) - 1)

str = ''
#print(l[0])#I don't know why there are two parts in this line???
print(str.join(l[0]).split(';'))

#print the number of attributes
number_of_attributes = len(str.join(l[0]).split(';'))
print(number_of_attributes)


l_fixed = []
for item in l:
    str =''
    l_item = str.join(item).split(';')
    l_fixed.append(l_item)





csv_file.close()
