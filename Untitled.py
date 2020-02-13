#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


df = pd.read_csv('example.txt')
df


# In[6]:


df = pd.read_csv('example.csv')
df


# In[7]:


import pandas as pd
import numpy as np


# In[8]:


from numpy.random import randn
np.random.seed(101)


# In[11]:


df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())


# In[12]:


df


# In[13]:


df['W']


# In[15]:


df[['W','Z']]


# In[16]:


df['NEW'] = df['W'] + df['Y']


# In[17]:


df


# In[26]:


df=df.drop('NEW',axis=1)


# In[19]:


df.loc['B','Y']


# In[20]:


df.loc[['A','B'],['W','Y']]


# In[21]:


df>0


# In[22]:


df<0


# In[27]:


df[df<0]


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}


# In[4]:


pd.Series(data=my_list)


# In[5]:


pd.Series(data=my_list,index=labels)


# In[ ]:




