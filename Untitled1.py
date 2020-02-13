#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


import numpy as np
x = np.linspace(0, 5, 11)
y = x ** 2


# In[5]:


x


# In[6]:


y


# In[16]:


plt.plot(x,y, 'black')
plt.xlabel('x axis title here')
plt.ylabel('y axis title here')
plt.title('string title here')
plt.show()


# In[32]:


plt.subplot(1,2,1)
plt.plot(x,y, 'r--')
plt.subplot(1,2,2)
plt.plot(y,x, 'b*-')


# In[33]:


fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x,y, 'black')
axes.set_xlabel('set x label')
axes.set_ylabel('set y label')
axes.set_title('set title')


# In[29]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y, 'b')
axes1.set_xlabel('x_label_axes2')
axes1.set_ylabel('y_label_axes2')
axes1.set_title('axes 1 title')

axes2.plot(y,x, 'r')
axes2.set_xlabel('x_label_axes2')
axes2.set_ylabel('y_label_axes2')
axes2.set_title('axes 2 title')


# In[35]:


fig, axes = plt.subplots(figsize=(12,3))

axes.plot(x,y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')


# In[37]:


fig.savefig("filename.png", dpi=200)


# In[38]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2, label="x**2")
ax.plot(x, x**2, label="x**3")
ax.legend()


# In[40]:


from random import sample
data = sample(range(1, 1000), 100)
plt.hist(data)


# In[ ]:




