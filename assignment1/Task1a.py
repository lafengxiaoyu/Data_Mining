import csv
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

def full_frame(width=None, height=None):
    import matplotlib as mpl
    mpl.rcParams['savefig.pad_inches'] = 0
    figsize = None if width is None else (width, height)
    fig = plt.figure(figsize=figsize)
    ax = plt.axes([0,0,0,0], frameon=False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.autoscale(tight=True)

l = []
with open("ODI-2019-csv.csv","r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        l.append(row)

# print the number of records
print ("The number of records: %d" %(len(l) - 1))

str = ''
# print(l[0])#I don't know why there are two parts in this line???
attributes = str.join(l[0]).split(';')
print("The attributes are: %s" % (attributes))

# print the number of attributes
number_of_attributes = len(str.join(l[0]).split(';'))
print ("The number of attributes: %d" %(number_of_attributes))

# fix the list of table
l_fixed = []
for item in l:
    str =''
    l_item = str.join(item).split(';')
    l_fixed.append(l_item)
del(l_fixed[0])

# plot the bar graph of one attributes
l_programme = []
l_gender = []
l_stress = []
l_euro = []
l_good_day = []
l_bed_time = []
l_chocolate = []
l_ML = []
l_IR = []
l_S = []
l_DB = []
l_stand =[]
for item in l_fixed:
    l_programme.append(item[1])
    l_ML.append(item[2])
    l_IR.append(item[3])
    l_S.append(item[4])
    l_DB.append(item[5])
    l_gender.append(item[6])
    l_chocolate.append(item[7])
    l_stand.append(item[10])
    l_euro.append(item[11])
    l_bed_time.append(item[13])
    l_good_day.append(item[14])
    l_stress.append(item[16])

l_ML_fixed = []
for item in l_ML:
    if item == 'yes':
        l_ML_fixed.append(1)
    else:
        l_ML_fixed.append(0)
l_IR_fixed = []
for item in l_IR:
    if item == '1':
        l_IR_fixed.append(1)
    else:
        l_IR_fixed.append(0)
l_S_fixed = []
for item in l_S:
    if item == 'mu':
        l_S_fixed.append(1)
    else:
        l_S_fixed.append(0)
l_DB_fixed = []
for item in l_DB:
    if item == 'ja':
        l_DB_fixed.append(1)
    else:
        l_DB_fixed.append(0)
l_gender_fixed = []
for item in l_gender:
    if item == 'male':
        l_gender_fixed.append(1)
    elif item == 'female':
        l_gender_fixed.append(2)
    else:
        l_gender_fixed.append(0)
l_chocolate_fixed = []
for item in l_chocolate:
    if item == 'slim':
        l_chocolate_fixed.append(1)
    elif item == 'fat':
        l_chocolate_fixed.append(2)
    elif item == 'neither':
        l_chocolate_fixed.append(3)
    elif item == 'unknown':
        l_chocolate_fixed.append(4)
    else:
        l_chocolate_fixed.append(0)
l_fixed_stand = []
for item in l_stand:
    if item == 'yes':
        l_fixed_stand.append(1)
    elif item =='no':
        l_fixed_stand.append(0)
    else:
        l_fixed_stand.append(2)


#plot correlation
df = pd.DataFrame({'ML': l_ML_fixed,
                   'IR': l_IR_fixed,
                   'Statistics': l_S_fixed,
                   'DB': l_DB_fixed,
                   'gender': l_gender_fixed,
                   'chocolate': l_chocolate_fixed,
                   'stand': l_fixed_stand
                   })
print(df.corr())
plt.clf()
sns.heatmap(df.corr(),cmap=sns.diverging_palette(220, 10, as_cmap=True))
plt.savefig('correlation_map.eps')
#sns.pairplot(df)


#deal with gender
full_frame()
plt.clf()
statistics_l_gender = pd.value_counts(l_gender)
statistics_l_gender_list = list(statistics_l_gender)
labels_gender = list(statistics_l_gender.index.values)
explode = (0.05,0.03,0.01)
plt.pie(x = statistics_l_gender_list, explode=explode,shadow= True,labels=labels_gender)
plt.savefig('gender_statistics.eps')
#deal with gender and chocolate
plt.clf()
df = pd.DataFrame({'A': l_gender,
                   'B': l_chocolate})

#print(df.groupby(['A', 'B']).count())
font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 23,
}
df.groupby('A')['B'].value_counts().unstack().plot(kind='bar', figsize=(12, 8))
plt.savefig('gender_chocolate.eps')

#deal with programme
statistics_l = pd.value_counts(l_programme)

statistics_l_programme_list = list(statistics_l)
labels = list(statistics_l.index.values)


def merge(name,original_name):
    for item in labels:
        if name != original_name:
            if name in item:
                index_number = labels.index(item)
                labels.remove(labels[index_number])
                index_number_origin = labels.index(original_name)
                statistics_l_programme_list[index_number_origin] += statistics_l_programme_list[index_number]
                statistics_l_programme_list.remove(statistics_l_programme_list[index_number])
        else:
            if name in item and name!=item:
                index_number = labels.index(item)
                labels.remove(labels[index_number])
                index_number_origin = labels.index(original_name)
                statistics_l_programme_list[index_number_origin] += statistics_l_programme_list[index_number]
                statistics_l_programme_list.remove(statistics_l_programme_list[index_number])

for item in labels:
    merge(item,item)

merge('Business Analytics','BA')
merge('Artificial Intelligence','AI')
merge('Artificial intelligence','AI')
merge('Ai','AI')
merge('ai','AI')
merge('Computational science','Computational Science')
merge('Computer Science','CS')
merge('computer science','CS')
merge('cs','CS')
#merge('Bioinf','Bioinformatics')
#merge('MSc Computational Science','Computational Science')


#print(len(statistics_l_programme_list))
#print(labels)
labels_cut = []
i = 0
for item in statistics_l_programme_list:
    if item < 3:
        labels_cut.append('')
    else:
        labels_cut.append(labels[i])
    i += 1

explode = (0.1,) * 3 +(0,) * (len(statistics_l_programme_list)-3)


plt.clf()
plt.pie(x = statistics_l_programme_list, explode=explode,shadow=True,labels=labels_cut)
plt.axis('off')
plt.tight_layout()
#plt.legend(loc='upper right')
plt.savefig('programme_statistics.eps')

#deal with bed time
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

l_bed_time_fixed = []
for item in l_bed_time:
    flag = 0
    if 'pm' in item or 'PM' in item or 'p.m' in item:
        flag = 1
    time = item.split(':')[0].split(' ')[0].split('a')[0].split('.')[0]
    if is_number(time):
        time = int(time)
        if flag == 1:
            time += 12
        if time == 12 or time == 24:
            time = 0
        if time>=0 and time <24:
            l_bed_time_fixed.append(time)


statistics_l = pd.value_counts(l_bed_time_fixed)

statistics_l_programme_list = list(statistics_l)
labels = list(statistics_l.index.values)
plt.clf()
plt.bar(labels,statistics_l_programme_list)
plt.savefig('bed_time_statistics.eps')

#deal with happy words
plt.clf()
str = ' '
chr_good_day = str.join(l_good_day)
wordcloud = WordCloud(background_color="white").generate(chr_good_day)
#full_frame()
plt.imshow(wordcloud,  interpolation='bilinear')
plt.axis("off")
plt.savefig('word_cloud.eps')


csv_file.close()
