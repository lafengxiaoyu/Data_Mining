
# coding: utf-8

# In[65]:


get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error


# In[51]:


data = pd.read_csv(r'.\winequality-red.csv')
data.tail()


# In[52]:


data_train, data_test = train_test_split(data, test_size=0.4, random_state=0)


# In[53]:


X = data_train.iloc[:,0:10].values
Y = data_train.iloc[:,11].values
X_t = data_test.iloc[:,0:10].values
Y_t = data_test.iloc[:,11].values


# In[63]:


# linear regression
lreg = linear_model.LinearRegression()
lreg.fit(X,Y)
Y_p = lreg.predict(X_t)
print("Linear Regression")
print("Mean squared error: %.2f" % mean_squared_error(Y_t, Y_p))
print("Mean absolute error: %.2f" % mean_absolute_error(Y_t, Y_p))


# In[89]:


# ridge regression, 
rreg = linear_model.Ridge()
rreg.fit(X,Y)
Y_p_r = rreg.predict(X_t)
print("Ridge Regression")
print("Mean squared error: %.2f" % mean_squared_error(Y_t, Y_p_r))
print("Mean absolute error: %.2f" % mean_absolute_error(Y_t, Y_p_r))


# In[90]:


# lasso regression
lareg = linear_model.Lasso()
lareg.fit(X,Y)
Y_p_l = lareg.predict(X_t)
print("Lasso Regression")
print("Mean squared error: %.2f" % mean_squared_error(Y_t, Y_p_l))
print("Mean absolute error: %.2f" % mean_absolute_error(Y_t, Y_p_l))


# In[93]:


# elasticnet regression
enreg = linear_model.ElasticNet()
enreg.fit(X,Y)
Y_p_en = enreg.predict(X_t)
print("ElasticNet Regression")
print("Mean squared error: %.2f" % mean_squared_error(Y_t, Y_p_en))
print("Mean absolute error: %.2f" % mean_absolute_error(Y_t, Y_p_en))

