#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np


# In[46]:


data = pd.read_csv("test_set_VU_DM.csv")


# In[47]:


probablities = np.round(np.random.rand(len(data)), 4)


# In[48]:


data['likelihood'] = probablities


# In[49]:


data = data.sort_values(['srch_id', 'likelihood'], ascending=[True, False])


# In[53]:


data = data.reset_index(drop = True)


# In[54]:


submit = data.filter(['srch_id', 'prop_id'], axis=1)


# In[52]:


submit.to_csv('submission_sample.csv', index=False)


# In[ ]:




