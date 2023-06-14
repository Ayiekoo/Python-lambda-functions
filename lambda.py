#!/usr/bin/env python
# coding: utf-8

# In[2]:


### the lambda function
# the function with no name(anonymoyus function)

(lambda x: x + 3)(3)

"""
lambda x

x + 3: is the expression being evaluated
takes '3' and adds it to the argument 'x'
"""


# In[3]:


(lambda x: x + 3)(7)


# In[4]:


(lambda x: x + 11)(3)


# In[5]:


### use of lambda in multiplication
multiply = lambda x, y: x * y
print(multiply(5, 4))


# In[6]:


multiply = lambda a, b: a * b
print(multiply(15, 7))


# In[7]:


#### square a number
square = lambda x: x ** 2
print(square(10))


# In[10]:


square = lambda x: x ** 2
print(square(11))


# In[8]:


## sorting a list of tuples by the second elements
list_of_tuples = [(1, 'd'), (2, 'b'), (3, 'c'), (4, 'a')]
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
print(sorted_list)


# In[9]:


### filtering a list using the lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers =list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# In[12]:


### create a list using lambda function
funcs = [(lambda x: x+n) for n in range(10)]
for f in funcs:
    print(f(0))


# In[13]:


### create a list using lambda function
funcs = [(lambda x: x+n) for n in range(5)]
for f in funcs:
    print(f(0))


# In[14]:


### checking is a string is a palindrone
is_palindrone = lambda s: s.lower() == s[::-1].lower()
print(is_palindrone("Madam"))


# In[15]:


### create a list using lambda function
funcs = [(lambda x: x+n) for n in range(5)]
for f in funcs:
    print(f(0))


# In[ ]:




