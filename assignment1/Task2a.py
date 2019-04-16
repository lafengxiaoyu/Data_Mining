import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm

train = pd.read_csv('titanic/train.csv', dtype={"Age": np.float64})
test = pd.read_csv('titanic/train.csv', dtype={"Age": np.float64})

train.info()
#plot
sns.barplot(x="Sex", y="Survived", data=train, palette='Blues')
plt.savefig('images2/Sex.eps')
plt.clf()
sns.barplot(x="SibSp", y="Survived", data=train, palette='Blues')
plt.savefig('images2/SibSp.eps')
plt.clf()
sns.barplot(x="Parch", y="Survived", data=train, palette='Blues')
plt.savefig('images2/Parch.eps')

pclass = np.array(train['Pclass'])
sibsp = np.array(train['SibSp'])


y = np.array(train['Survived'])
c = np.vstack((pclass,sibsp))
x = map(list,zip(*c))

clf = svm.SVR()
clf.fit(x, y)

print(clf.predict([[-0.8, -1]]))