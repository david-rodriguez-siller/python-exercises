#!/usr/bin/env python
# coding: utf-8

# ### Conditional Basics

# #### a. prompt the user for a day fo the week, print out whether the day is Monday or not

# In[4]:


def is_today_monday():
    weekday = input("Enter the day of the week: ")
    if weekday.lower() == 'monday':
        print("Today is Monday! Happy beginning of the week!")
    else:
        print("Today is not Monday. You're one day closer to the weekend!")


# In[5]:


is_today_monday()


# #### b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# In[23]:


def is_it_the_weekend():
    weekday = input("Enter the day of the week: ")
    if weekday.lower() == 'saturday' or weekday.lower() == 'sunday':
        print("Today is {}! Happy weekend!".format(weekday.capitalize()))
    else:
        print("Today is {}. It is not the weeked. :( ".format((weekday.capitalize())))


# In[24]:


is_it_the_weekend()


# #### c. create variables and make up values for
#  - the number of hours worked in one week
#  - the hourly rate
#  - how much the week's paycheck will be
# 
# #### write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[166]:


hours_worked = int(input("How many hours did you work last week? "))
hourly_rate = int(input("What is your hourly rate? "))
overtime_rate = hourly_rate * 1.5
if hours_worked <= 40:
    weekly_wages = print("Your weekly wages are: ${}".format(hours_worked * hourly_rate))
else:
    weekly_wages = print("Your weekly wages are: ${}".format(40 * hourly_rate + (hours_worked - 40) * overtime_rate))


# ### Loop Basics

# ### While
#  - Create an integer variable i with a value of 5.
#  - Create a while loop that runs so long as i is less than or equal to 15
#  - Each loop iteration, output the current value of i, then increment i by one.

# In[161]:


i = 5
while i <= 14:
    i = i + 1
    print(i)


#  - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# In[28]:


loops_by_two = 0
while loops_by_two <= 100:
    print(loops_by_two)
    loops_by_two = loops_by_two + 2


#  - Alter your loop to count backwards by 5's from 100 to -10.

# In[32]:


loops_by_five = 100
while loops_by_five >= -10:
    print(loops_by_five)
    loops_by_five = loops_by_five - 5


#  - Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.

# In[33]:


squared_loops = 2
while squared_loops <= 1000000:
    print(squared_loops)
    squared_loops = squared_loops ** 2


#  - Write a loop that uses print to decrease from value 100 to 5

# In[35]:


loops_by_five = 100
while loops_by_five > 0:
    print(loops_by_five)
    loops_by_five = loops_by_five - 5


# ### For
#  - Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number
#  - Create a for loop that uses print

# In[42]:


numb_mult = int(input("Enter a number: "))
for number in range(1,11):
    output = numb_mult * number
    print("{} x {} = ".format(numb_mult, number), output)


# In[43]:


print('2' * 2)


# In[45]:


numb = 1
for number in range (1,10):
    print(str(numb) * number)
    numb = numb + 1


# ###  Break and Continue

#  - Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# In[173]:


odd_number = int(input("Odd number to skip is: "))
if type(odd_number) != int or odd_number % 2 == 0:
    print("Invalid input. Please enter an odd number between 1 and 50")
if type(odd_number) == int:
    if odd_number % 2 != 0 and odd_number <= 50 and odd_number >= 1:    
        for number in range(1, 50):
            if number % 2 != 0 and number == odd_number:
                print("Yikes! Skipping number: {}".format(number))
            elif number % 2 != 0:
                print("Here is an odd number: {}".format(number))                


#  - The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# In[176]:


posi_numb = int(input("Enter a positive number: "))
if posi_numb > 0:
    for number in range(0, posi_numb + 1):
        print(number)
else:
    print("You did not enter a positive number")


#  - Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1

# In[177]:


posi_numb = int(input("Enter a positive number: "))
while posi_numb >= 1:
    print(posi_numb)
    posi_numb = posi_numb - 1
if posi_numb < 0:
    print("You did not enter a positive number")


# ### Fizzbuzz
# 
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills

#  - Write a program that prints the numbers from 1 to 100

# In[67]:


counter = 1
while counter <= 100:
    print(counter)
    counter = counter + 1


#  - For multiples of three print "Fizz" instead of the number

# In[178]:


counter = 1
while counter <= 100:
    if counter % 3 == 0:
        print('Fizz')
    else:    
        print(counter)
    counter = counter + 1


#  - For the multiples of five print "Buzz"

# In[70]:


counter = 1
while counter <= 100:
    if counter % 5 == 0:
        print('Buzz')
    else:    
        print(counter)
    counter = counter + 1


#  - For numbers which are multiples of both three and five print "FizzBuzz"

# In[180]:


counter = 1
while counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print('FizzBuzz')
    elif counter % 3 == 0:
        print('Fizz')
    elif counter % 5 == 0:
        print('Buzz')
    else:    
        print(counter)
    counter = counter + 1


# ### Display a table of powers
#  - Prompt the user to enter an integer.
#  - Display a table of squares and cubes from 1 to the value entered.
#  - Ask if the user wants to continue.
#  - Assume that the user will enter valid data.
#  - Only continue if the user agrees to.

# In[118]:


from tabulate import tabulate
table = []
continue_loop = input("Would you like to get started?(y/n) ")
while continue_loop == 'y':
    table_of_powers = int(input("What number would you like to go up to? "))
    for number in range(1, table_of_powers + 1):
        table.append([number, number ** 2, number * number * number])   
    print(tabulate(table, headers = ["Number", "Squared", "Cubed"]))
    table = []
    continue_loop = input("Would you like to continue?(y/n) ")
else:
    print("See ya!")


# ### Convert given number grades into letter grades
#  - Prompt the user for a numerical grade from 0 to 100.
#  - Display the corresponding letter grade.
#  - Prompt the user to continue.
#  - Assume that the user will enter valid integers for the grades.
#  - The application should only continue if the user agrees to.
#  - Grade Ranges:
# 
#   - A : 100 - 88
#   - B : 87 - 80
#   - C : 79 - 67
#   - D : 66 - 60
#   - F : 59 - 0

# In[114]:


continue_loop = input("Would you like to know your letter grade?(y/n) ")
while continue_loop == 'y':
    grade = int(input("What is your numerical grade? "))
    if grade >= 88:
        print("Your grade is A")
    elif grade >= 80:
        print("Your grade is B")
    elif grade >= 67:
        print("Your grade is C")
    elif grade >= 60:
        print("Your grade is D")
    else:
        print("Your grade is F")
    continue_loop = input("Would you like to know your letter grade?(y/n) ")
else:
    print("See ya!")


# ### Bonus
#  - Edit your grade ranges to include pluses and minuses

# In[115]:


continue_loop = input("Would you like to know your letter grade?(y/n) ")
while continue_loop == 'y':
    grade = int(input("What is your numerical grade? "))
    if grade >= 97:
        print("Your grade is A+")
    elif grade >= 94:
        print("Your grade is A")        
    elif grade >= 90:
        print("Your grade is A-")
    elif grade >= 87:
        print("Your grade is B+")        
    elif grade >= 84:
        print("Your grade is B")
    elif grade >= 80:
        print("Your grade is B-")
    elif grade >= 77:
        print("Your grade is C+")
    elif grade >= 74:
        print("Your grade is C")
    elif grade >= 70:
        print("Your grade is C-")        
    elif grade >= 67:
        print("Your grade is D+")
    elif grade >= 64:
        print("Your grade is D")
    elif grade >= 60:
        print("Your grade is D-")
    else:
        print("Your grade is F")
    continue_loop = input("Would you like to know your letter grade?(y/n) ")
else:
    print("See ya!")


# ### Create a list of dictionaries
#  - Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
#   - Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[142]:


book_list = [
    {'title':'The Alchemist', 'author':'Paulo Coelho', 'genre':'Fiction'},
    {'title':'The Undocumented Americans', 'author':'Karla Villavicencio', 'genre':'Non-Fiction'},
    {'title':'Slaughterhouse-five', 'author':'Kurt Vonnegut Jr.', 'genre':'Sci-Fi'},
    {'title': 'Maus', 'author':'Art Spiegelman', 'genre':'Graphic Novel'}
]
print(book_list)


# In[187]:


for book in book_list:
    print(f"The book title is: {book['title']}. The book author is: {book['author']}. The book genre is: {book['genre']}")


# In[153]:


genre_input = input("Enter a book genre: ")
for book in book_list:
    if genre_input == book['genre']:
        print(book)


# In[ ]:




