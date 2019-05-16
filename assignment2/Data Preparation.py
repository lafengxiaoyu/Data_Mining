#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'qt')


# In[32]:


data = pd.read_csv("training_set_VU_DM.csv")
data.shape


# In[33]:


columns = data.keys()
for column in columns:
    if (1-data[column].count()/len(data))>0.9:
        print(column)
        data.drop([column], axis=1, inplace=True)
data.shape


# In[62]:


print("columns and missing data")
print("total_columns:", len(data.columns))
round((1-data.count()/len(data))*100, 2)


# In[35]:


# dropping competitor columns
comps = [col for col in data.columns if (col[-3:] == 'iff' or col[-3:] == 'inv')]
for c in comps:
    data.drop([c], axis=1, inplace= True)


# In[36]:


# dropping date_time
data.drop(['date_time'], axis=1, inplace=True)


# In[50]:


sns.heatmap(round(data.corr(),2),annot=True, xticklabels=True, yticklabels=True)


# In[53]:


#correlation cutoff = 0.44
# From the correlation map, I am only oncsidering two competitors for now. with the lesser missing values
data.drop(['comp3_rate','comp8_rate'], axis=1, inplace=True)

# There are two location scores, since they are correlated, we will just look at one. The one without any missing values
data.drop(['prop_location_score2'], axis=1, inplace=True)

# Similar agruemnt for star rating and review score, the latter is dropped
data.drop(['prop_review_score'], axis=1, inplace=True)


# In[54]:


#Intuitively the physical distance shoudnt play a greater role than the information available from search country and property country/
# Please argue if you feel otherwise
data.drop(['orig_destination_distance'], axis=1, inplace=True)


# In[56]:


#Same argument for site_id
data.drop(['site_id'], axis=1, inplace=True)


# In[58]:


#Also from the correlation, number of rooms and adult count seems to be correlated. So dropping one here.
data.drop(['srch_room_count'], axis=1, inplace=True)


# In[59]:


data.fillna(0, inplace=True)


# In[ ]:


data.to_csv("training_version1.csv")


# In[ ]:




