#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


print(os.listdir())


# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


dataFrame = pd.read_csv('911.csv')


# In[6]:


dataFrame


# In[9]:


# top 5 zip codes
dataFrame['zip'].value_counts().head(5)


# In[10]:


#top 5 township call 911
dataFrame['twp'].value_counts().head(5)


# In[11]:


#Count the number of unique reasons
dataFrame['title'].nunique()


# In[15]:


dataFrame['SpecificReason'] = dataFrame['title'].apply(lambda title: title.split(':')[1])


# In[16]:


dataFrame.head()


# In[21]:


dataFrame['SpecificReason'].value_counts().head(10)


# In[22]:


dataFrame['SpecificReasonCategory'] = dataFrame['title'].apply(lambda title: title.split(':')[0])


# In[23]:


dataFrame


# In[27]:


dataFrame['SpecificReasonCategory'].value_counts()


# In[30]:


sns.countplot(x='SpecificReasonCategory', data=dataFrame)


# In[31]:


dataFrame['timeStamp'] = pd.to_datetime(dataFrame['timeStamp'])


# In[32]:


dataFrame


# In[33]:


dataFrame.info()


# In[34]:


dataFrame['Hour'] = dataFrame['timeStamp'].apply(lambda time: time.hour)


# In[35]:


dataFrame


# In[38]:


dataFrame['Month'] = dataFrame['timeStamp'].apply(lambda time: time.month)
dataFrame['DayofWeek'] = dataFrame['timeStamp'].apply(lambda time: time.dayofweek)


# In[42]:


dataFrame.head()


# In[51]:


sns.countplot(x='Month', data=dataFrame, hue='SpecificReasonCategory',edgecolor=sns.color_palette("dark", 3))
plt.legend(loc='best', bbox_to_anchor=(1,1))


# In[52]:


byMonth = dataFrame.groupby('Month').count()


# In[53]:


byMonth


# In[64]:


byMonth['twp'].plot()
plt.legend(loc='best', bbox_to_anchor=(1.225,1))


# In[65]:


byDays = dataFrame.groupby('DayofWeek').count()


# In[66]:


byDays['twp'].plot()
plt.legend(loc='best', bbox_to_anchor=(1.225,1))


# In[ ]:




