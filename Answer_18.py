#!/usr/bin/env python
# coding: utf-8

# In[23]:


"""18. Implement a decorator function called ‘timer’ that measures the execution time of a function. The ‘timer’ decorator should print the time taken by the decorated function to execute. Use the ‘time’ module in Python to calculate the execution time.

Example:

import time

@timer
def my_function():
    # Function code goes here
    time.sleep(2)

my_function()

Output:
"Execution time: 2.00123 seconds"""


# In[47]:


import time


# In[57]:


def timer(func):
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.5f} seconds")
        return result
    return wrap


# In[58]:


@timer
def sum(x,y):
    return (x+y)


# In[59]:


sum(2,6)


# In[ ]:




