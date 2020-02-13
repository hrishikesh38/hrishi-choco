#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# # read in the cv file as a dataframe called df

# In[3]:


df = pd.read_csv('911.csv')


# In[4]:


df.info()


# In[5]:


df.head(3)


# In[6]:


df.tail(3)


# # basic question
# ## what are the top 5 zipcodes for 911 calls?

# In[7]:


df['zip'].value_counts().head(5)


# ## what are the top 5 township for 911 calls?

# In[9]:


df['twp'].value_counts().head(5)


# In[10]:


df['reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[11]:


df['reason'].value_counts()


# In[12]:


sns.countplot(x='reason',data=df,palette='viridis')


# In[14]:


df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[15]:


df['hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['month'] = df['timeStamp'].apply(lambda time: time.month)
df['day of week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[16]:


dmap = {0:'mon',1:'tue',2:'wed',3:'wed',4:'thur',5:'fri',6:'sun'}


# In[17]:


df['day of week'] = df['day of week'].map(dmap)


# In[23]:


sns.countplot(x='day of week',data=df,hue='reason',palette='viridis')

plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)


# In[ ]:




