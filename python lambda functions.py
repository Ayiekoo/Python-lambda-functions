#!/usr/bin/env python
# coding: utf-8

# In[2]:


###### Python lambda functions ////// anonymous functions #####

square = lambda num:num * num
print(square(12))


# In[3]:


examp_list = [10, 5, 15, 6]
squares = list(map(lambda num:num * num, examp_list))
print(squares)


# In[4]:


examp_list = [100, 55, 155, 66]
squares = list(map(lambda num:num * num, examp_list))
print(squares)


# In[ ]:




