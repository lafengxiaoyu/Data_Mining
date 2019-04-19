
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


# In[15]:


sms_data = pd.read_csv(r'.\SmsCollection.csv', sep = ';', usecols = ['label', 'text'])#, error_bad_lines = False, warn_bad_lines = False)
sms_data.head()


# In[25]:


X = sms_data['text'].values
Y = sms_data['label'].values
# Transformation
cv = CountVectorizer()
X = cv.fit_transform(X.astype('U')) 


# In[36]:


# cross validation
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# Naive Bayes Classifier
cl = MultinomialNB()
cl.fit(X_train, Y_train)
cl.score(X_test, Y_test)
Y_p = cl.predict(X_test)
print(classification_report(Y_test,Y_p))

