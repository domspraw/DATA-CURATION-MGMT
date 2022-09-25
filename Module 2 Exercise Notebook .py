#!/usr/bin/env python
# coding: utf-8

# ## Q1 (2 points)
# Convert a list of multiple integers into a single integer:
# 
# Sample list: [11, 33, 50]
# 
# Expected Output: 113350

# In[1]:


a = [11, 33, 50]


# In[2]:


# Write your program here. The cell output should be the integer 113350.

#Create a List 

a = [11, 33, 50] 
for i in a:
    print(i, end="")
    


# ## Q2 (3 points)
# Flatten a given nested list structure. 
# 
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# 
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# In[1]:


a = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]


# In[17]:


# Write your program here. The cell output should be the flattened list.
def flatlist(a):
    flatten_a = []
    for element in a:
        if type(element) is list:
            for item in element:
                flatten_a.append(item)
        else:
            flatten_a.append(element)
    return flatten_a

print(a)
print(flatlist(a))
    


# ## Q3 (2 points)
# Convert a given dictionary into a list of lists.
# 
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# 
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]

# In[7]:


myDict = {
    1: 'red',
    2: 'green',
    3: 'black',
    4: 'white',
    5: 'black'
}


# In[14]:


# Write your program here. The cell output should be the list of lists
def LofL(myDict):
    result = list(map(list, myDict.items()))
    return result    

print("Original Dictionary:")
print(myDict)
print("list of lists:")
print(LofL(myDict))


# ## Q4 (3 points)
# Create a new GitHub repository. Save this notebook to that repository, and enter the link to the GitHub repository below. 

# 

# https://github.com/domspraw/DATA-CURATION-MGMT.git
