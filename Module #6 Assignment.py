#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys 


# In[2]:


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print("{0}\t{1}".format(item, cost))


# In[3]:


import sys

from datetime import datetime
from datetime import time
from datetime import date


# In[4]:


def main():
    
    dt = datetime.now()
    
    time_string = dt.strftime("%X")
    
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            _date,_time,store,item,cost,payment = data
            print("{dt}\t{time_string}\t{store}\t{item}\t{cost}\t{payment}")


# In[5]:


main()


# In[6]:


datetime.now()


# In[ ]:





# In[7]:


from datetime import timedelta


# In[8]:


import datetime


# In[12]:


x = -60
y = 104
z = 1

result = datetime.datetime.now() + datetime.timedelta(seconds = x, weeks = y)


# In[13]:


result


# In[ ]:





# In[14]:


result2 = datetime.datetime.now() + datetime.timedelta(days = z)


# In[15]:


result2


# In[ ]:





# In[13]:


from datetime import timedelta


# In[14]:


d = timedelta(days = 100, hours = 10, minutes = 13)


# In[15]:


print(d)


# In[ ]:





# In[16]:


from datetime import datetime


# In[17]:


datetime_object = datetime.now()


# In[18]:


print(datetime_object)


# In[19]:


print('Type :- ', type(datetime_object))


# In[20]:


class new_datetime:
    
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        self.time = datetime.now()
    
    def myfunc(self):
        print(("Feet: {0}, Inches: {1}, Time created: {2}").format(self.feet, self.inches, self.time))


# In[22]:


new_object = new_datetime(14,15)

print(new_object.myfunc())


# In[ ]:




