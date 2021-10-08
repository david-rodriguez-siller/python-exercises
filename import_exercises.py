#!/usr/bin/env python
# coding: utf-8

# ### Import Exercises

# #### 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
#  - Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
#  - Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.
#  - Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.
#  
# Make sure our code that tests the function imports is run from the same directory that your functions exercise file is in.

# #### .syntax

# In[22]:


import function_exercises as fe
sample_string = 'a'
fe.is_vowel(sample_string)


# #### from

# In[23]:


from function_exercises import calculate_tip


# In[24]:


calculate_tip(.2, 100)


# #### from alias

# In[26]:


from function_exercises import get_letter_grade as glg


# In[27]:


glg(94)


# #### 2. Read about and use the itertools module from the python standard library to help you solve the following problems:
#  - How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
#  - How many different combinations are there of 2 letters from "abcd"?
#  - How many different permutations are there of 2 letters from "abcd"?

# In[44]:


import itertools

counter = 0
for item in itertools.permutations('abc123', 6):
    counter = counter + 1
print('There are {} different ways to combine letters a, b and c with numbers 1, 2, and 3.'.format(counter))


# In[47]:


counter = 0
for item in itertools.combinations('abcd', 2):
    counter = counter + 1
print('There are {} different combinations of 2 letters from letters a, b, c, and d.'.format(counter))


# In[48]:


counter = 0
for item in itertools.permutations('abcd', 2):
    counter = counter + 1
print('There are {} different permutations of 2 letters from letters a, b, c, and d.'.format(counter))


# #### 3. Save this file as profiles.json inside of your exercises directory (right click -> save file as...). Use the load function from the json module to open this file.
# 
# Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
# 
#  - Total number of users
#  - Number of active users
#  - Number of inactive users
#  - Grand total of balances for all users
#  - Average balance per user
#  - User with the lowest balance
#  - User with the highest balance
#  - Most common favorite fruit
#  - Least most common favorite fruit
#  - Total number of unread messages for all users

# In[53]:


import json

profiles = json.load(open('profiles.json'))


# #### Total number of users

# In[56]:


counter = 0
for item in profiles:
    counter = counter + 1
print('The total number of users is: {}'.format(counter))


# #### Number of active users

# In[57]:


counter = 0
for item in profiles:
    if item['isActive'] == True:
        counter = counter + 1
print('The total number of active users is: {}'.format(counter))


# #### Number of inactive users

# In[58]:


counter = 0
for item in profiles:
    if item['isActive'] == False:
        counter = counter + 1
print('The total number of inactive users is: {}'.format(counter))


# #### Grand total of balances for all users

# In[122]:


balance = 0
for item in profiles:
    remove = item['balance'].replace('$', '').replace(',', '')
    balance = float(remove) + balance
print('The grand total of balances for all users is: ${:,}'.format(balance))


# #### Average balance per user

# In[146]:


balance = 0
counter = 0
for item in profiles:
    remove = item['balance'].replace('$', '').replace(',', '')
    balance = float(remove) + balance
for item in profiles:
    counter = counter + 1

a_b = '{0:,.2f}'.format(balance / counter)

print('The average balance per user is: ${}'.format(a_b))


# #### User with the lowest balance

# In[80]:


lst = []
user = 0
for item in profiles:
    lst.append(item['balance'])
for item in profiles:
    if item['balance'] == min(lst):
        user = item['name']
print('The user with the lowest balance is: {}'.format(user))


# #### User with the highest balances

# In[81]:


lst = []
user = 0
for item in profiles:
    lst.append(item['balance'])
for item in profiles:
    if item['balance'] == max(lst):
        user = item['name']
print('The user with the lowest balance is: {}'.format(user))


# #### Most common favorite fruit

# In[85]:


lst = []
for item in profiles:
    lst.append(item['favoriteFruit'])
def most_common(fruit):
    mcf = max(set(fruit), key = fruit.count)
    print('The most common favorite fruit is: {}'.format(mcf))
most_common(lst)


# #### Least most common favorite fruit

# In[87]:


lst = []
for item in profiles:
    lst.append(item['favoriteFruit'])
def least_common(fruit):
    lcf = min(set(fruit), key = fruit.count)
    print('The least common favorite fruit is: {}'.format(lcf))
least_common(lst)


# #### Total number of unread messages for all users

# In[120]:


greetings = []
counter = 0
for item in profiles:
    greetings.append(item['greeting'])
for word in greetings:
    split_list = word.split()
    counter = counter + int(split_list[-3])
print("The total number of unread messages for all users is: {}".format(counter))

