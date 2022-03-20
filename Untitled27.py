#!/usr/bin/env python
# coding: utf-8

# In[21]:


#importing the necessary libraries
import numpy as np
import pandas as pd


# In[26]:


#importing the dataset
users = pd.read_table(r"C:\Users\sanje_crlv28m\Downloads\u.user.txt")
users.head()


# In[15]:


#First 10 entries
users.head(10)   


# In[16]:


#last 10 entries
users.tail(10)  


# In[30]:


#What is the number of observations in the dataset?
users.shape


# In[31]:


#Print the name of all the columns.
users.columns


# In[36]:


ncols = users.shape[1]
ncols


# In[38]:


#What is the data type of each column?
users.dtypes 


# In[40]:


#DataFrame Info?
users.info


# In[48]:


#Describe all the columns
users.describe(include='all')  


# In[ ]:




