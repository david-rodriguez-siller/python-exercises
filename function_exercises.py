#!/usr/bin/env python
# coding: utf-8

# ### Function Exercises

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[ ]:


def is_two(number):
    if str(number.lower()) == 'two' or int(number) == 2:
        return True
    else:
        return False
        
is_two('twO')


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[ ]:


def is_vowel(string):
    if len(string) > 1:
        print("You must enter a single character string.")
    vowels = 'aeiou'
    string = str(string)
    string = string.lower()
    
    for letter in string:
        if letter in vowels:
            return True
        else:
            return False
        
is_vowel('a')


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[ ]:


def is_consonant(string):
    if len(string) > 1:
        print("You must enter a single character string.")
    consonants = 'bcdfghjklmnpqrstvwxyz'
    string = str(string)
    string = string.lower()
    
    for letter in string:
        if letter in consonants:
            return True
        else:
            return False
        
is_consonant('z')       


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[ ]:


def cap_con(string):
    if ' ' in string:
        print("You must enter a single word string.")
        return
    consonants = 'bcdfghjklmnpqrstvwxyz'
    string = str(string)
    if string[0] in consonants:
        return string.capitalize()
    
cap_con('cool')


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[ ]:


def calculate_tip(tip_percentage, bill_total):
    if tip_percentage > 1 or tip_percentage < 0:
        print("You must enter your tip percentage as a number between 0 and 1.")
    print("Your bill total is: ${}".format(bill_total))
    print("Your desired {}% tip is: ${}".format(tip_percentage * 100, tip_percentage * bill_total))

calculate_tip(.2, 100)


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[ ]:


def apply_discount(original_price, discount_percentage):
    print("The original price of this item is: ${}".format(original_price))
    print("There is a {}% discount. The price after applying the discount is: ${}".format(discount_percentage, original_price - (original_price * discount_percentage * .01)))
    
apply_discount(100, 20) 


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[ ]:


def handle_commas():
    user_input = input('Enter a string made up of numbers and commas: ')

    user_input = user_input.replace(',', '')
    if user_input.isdigit():
        return user_input
    else:
        print('Your input must contain commas/numbers.')

handle_commas()


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[ ]:


def get_letter_grade(score):
    score = int(score)
    if score > 100:
        print("Please enter a grade between 0 and 100.")
    elif score >= 90:
        print("Your grade is A")
    elif score >= 80:
        print("Your grade is B")
    elif score >= 70:
        print("Your grade is C")
    elif score >= 60:
        print("Your grade is D")
    else:
        print("Your grade is F")
        
get_letter_grade(93)


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[ ]:


def remove_vowels(text):
    vowels = 'aeiou'
    no_vowels = text
    if type(text) != str:
        print('Your input format must be in string.')
    for letter in text:
        if letter in vowels:
            no_vowels = no_vowels.replace(letter, '')
    return no_vowels

remove_vowels('good morning')


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#  - Name will become name
#  - First Name will become first_name
#  - % Completed will become completed

# In[ ]:


def normalize_name(text):
    import string
    valid_characters = string.ascii_lowercase + '1234567890_'
    text = text.lower()
    normalized = text
    normalized = normalized.strip()
    normalized = normalized.replace(' ', '_')
    for letter in normalized:
        if letter not in valid_characters:
            normalized = normalized.replace(letter, '')
        return normalized

normalize_name('.dav')


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[ ]:


sample_lst = [1, 2, 3, 4, 5, '6']
def cumulative_sum(lst):
    counter = 0
    for item in lst:
        if type(item) != int:
            counter = counter + 1
    if counter >= 1:
         print('Your list must be made up of numbers only.')
    sum_acc = 0
    function_lst = []
    if counter == 0:
        for item in lst:
            sum_acc = sum_acc + item
            function_lst.append(sum_acc)
        return function_lst

cumulative_sum(sample_lst)


# #### Additional Exercise
# - Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

# #### Bonus
# 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# In[19]:


def twelveto24():
#    import re
#    what_time = input('Enter the current time in hours and minutes: ')
#    if re.match(':', what_time):
#        print('You entered: {}'.format(what_time))
#        am_pm = input('is it am or pm? ').lower()
#        if am_pm == 'am' or am_pm == 'pm':
#            print('You entered: {}'.format(am_pm))
#            output_time = what_time + am_pm
#        else:
#            print('Enter am or pm only.')
#    else:
#        print('Enter your time in this format: HH:SS')


# In[20]:


twelveto24()


# 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
#  - col_index('A') returns 1
#  - col_index('B') returns 2
#  - col_index('AA') returns 27

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




