#!/usr/bin/env python
# coding: utf-8

# In[4]:


""""17. Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from the input list. Use list comprehension to solve this problem.

Example:

Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Output: [2, 4, 6, 8, 10"""


# In[18]:


def even_num(num):
    return [num for num in num if num%2==0]


# In[19]:


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[20]:


even_number = even_num(list)


# In[21]:


print(even_number)


# In[ ]:




