{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "37717a00",
   "metadata": {},
   "source": [
    "### Conditional Basics"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "85d6d627",
   "metadata": {},
   "source": [
    "#### a. prompt the user for a day fo the week, print out whether the day is Monday or not"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4b165f31",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_today_monday():\n",
    "    weekday = input(\"Enter the day of the week: \")\n",
    "    if weekday.lower() == 'monday':\n",
    "        print(\"Today is Monday! Happy beginning of the week!\")\n",
    "    else:\n",
    "        print(\"Today is not Monday. You're one day closer to the weekend!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2b516622",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the day of the week: tuesday\n",
      "Today is not Monday. You're one day closer to the weekend!\n"
     ]
    }
   ],
   "source": [
    "is_today_monday()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dca02cdb",
   "metadata": {},
   "source": [
    "#### b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "45631867",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_it_the_weekend():\n",
    "    weekday = input(\"Enter the day of the week: \")\n",
    "    if weekday.lower() == 'saturday' or weekday.lower() == 'sunday':\n",
    "        print(\"Today is {}! Happy weekend!\".format(weekday.capitalize()))\n",
    "    else:\n",
    "        print(\"Today is {}. It is not the weeked. :( \".format((weekday.capitalize())))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "9334f54d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the day of the week: monday\n",
      "Today is Monday. It is not the weeked. :( \n"
     ]
    }
   ],
   "source": [
    "is_it_the_weekend()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "65f931f8",
   "metadata": {},
   "source": [
    "#### c. create variables and make up values for\n",
    " - the number of hours worked in one week\n",
    " - the hourly rate\n",
    " - how much the week's paycheck will be\n",
    "\n",
    "#### write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "1ae0c151",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How many hours did you work last week? 45\n",
      "What is your hourly rate? 25\n",
      "Your weekly wages are: $1187.5\n"
     ]
    }
   ],
   "source": [
    "hours_worked = int(input(\"How many hours did you work last week? \"))\n",
    "hourly_rate = int(input(\"What is your hourly rate? \"))\n",
    "overtime_rate = hourly_rate * 1.5\n",
    "if hours_worked <= 40:\n",
    "    weekly_wages = print(\"Your weekly wages are: ${}\".format(hours_worked * hourly_rate))\n",
    "else:\n",
    "    weekly_wages = print(\"Your weekly wages are: ${}\".format(40 * hourly_rate + (hours_worked - 40) * overtime_rate))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0ff5922b",
   "metadata": {},
   "source": [
    "### Loop Basics"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45dc508d",
   "metadata": {},
   "source": [
    "### While\n",
    " - Create an integer variable i with a value of 5.\n",
    " - Create a while loop that runs so long as i is less than or equal to 15\n",
    " - Each loop iteration, output the current value of i, then increment i by one."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "4fae6523",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "i = 5\n",
    "while i <= 14:\n",
    "    i = i + 1\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8dc0f648",
   "metadata": {},
   "source": [
    " - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "5e4010e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n",
      "52\n",
      "54\n",
      "56\n",
      "58\n",
      "60\n",
      "62\n",
      "64\n",
      "66\n",
      "68\n",
      "70\n",
      "72\n",
      "74\n",
      "76\n",
      "78\n",
      "80\n",
      "82\n",
      "84\n",
      "86\n",
      "88\n",
      "90\n",
      "92\n",
      "94\n",
      "96\n",
      "98\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "loops_by_two = 0\n",
    "while loops_by_two <= 100:\n",
    "    print(loops_by_two)\n",
    "    loops_by_two = loops_by_two + 2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3637e45e",
   "metadata": {},
   "source": [
    " - Alter your loop to count backwards by 5's from 100 to -10."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "5cf436c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n",
      "0\n",
      "-5\n",
      "-10\n"
     ]
    }
   ],
   "source": [
    "loops_by_five = 100\n",
    "while loops_by_five >= -10:\n",
    "    print(loops_by_five)\n",
    "    loops_by_five = loops_by_five - 5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4157752f",
   "metadata": {},
   "source": [
    " - Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "82881ae8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "16\n",
      "256\n",
      "65536\n"
     ]
    }
   ],
   "source": [
    "squared_loops = 2\n",
    "while squared_loops <= 1000000:\n",
    "    print(squared_loops)\n",
    "    squared_loops = squared_loops ** 2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6dc12f27",
   "metadata": {},
   "source": [
    " - Write a loop that uses print to decrease from value 100 to 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "5d577e5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "loops_by_five = 100\n",
    "while loops_by_five > 0:\n",
    "    print(loops_by_five)\n",
    "    loops_by_five = loops_by_five - 5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f8895341",
   "metadata": {},
   "source": [
    "### For\n",
    " - Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number\n",
    " - Create a for loop that uses print"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "c4f0ac42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 2\n",
      "2 x 1 =  2\n",
      "2 x 2 =  4\n",
      "2 x 3 =  6\n",
      "2 x 4 =  8\n",
      "2 x 5 =  10\n",
      "2 x 6 =  12\n",
      "2 x 7 =  14\n",
      "2 x 8 =  16\n",
      "2 x 9 =  18\n",
      "2 x 10 =  20\n"
     ]
    }
   ],
   "source": [
    "numb_mult = int(input(\"Enter a number: \"))\n",
    "for number in range(1,11):\n",
    "    output = numb_mult * number\n",
    "    print(\"{} x {} = \".format(numb_mult, number), output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "f21fbb61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n"
     ]
    }
   ],
   "source": [
    "print('2' * 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "5810ec10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "22\n",
      "333\n",
      "4444\n",
      "55555\n",
      "666666\n",
      "7777777\n",
      "88888888\n",
      "999999999\n"
     ]
    }
   ],
   "source": [
    "numb = 1\n",
    "for number in range (1,10):\n",
    "    print(str(numb) * number)\n",
    "    numb = numb + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6eab08df",
   "metadata": {},
   "source": [
    "###  Break and Continue"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "43a2aff7",
   "metadata": {},
   "source": [
    " - Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "id": "8756ea9b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Odd number to skip is: 3\n",
      "Here is an odd number: 1\n",
      "Yikes! Skipping number: 3\n",
      "Here is an odd number: 5\n",
      "Here is an odd number: 7\n",
      "Here is an odd number: 9\n",
      "Here is an odd number: 11\n",
      "Here is an odd number: 13\n",
      "Here is an odd number: 15\n",
      "Here is an odd number: 17\n",
      "Here is an odd number: 19\n",
      "Here is an odd number: 21\n",
      "Here is an odd number: 23\n",
      "Here is an odd number: 25\n",
      "Here is an odd number: 27\n",
      "Here is an odd number: 29\n",
      "Here is an odd number: 31\n",
      "Here is an odd number: 33\n",
      "Here is an odd number: 35\n",
      "Here is an odd number: 37\n",
      "Here is an odd number: 39\n",
      "Here is an odd number: 41\n",
      "Here is an odd number: 43\n",
      "Here is an odd number: 45\n",
      "Here is an odd number: 47\n",
      "Here is an odd number: 49\n"
     ]
    }
   ],
   "source": [
    "odd_number = int(input(\"Odd number to skip is: \"))\n",
    "if type(odd_number) != int or odd_number % 2 == 0:\n",
    "    print(\"Invalid input. Please enter an odd number between 1 and 50\")\n",
    "if type(odd_number) == int:\n",
    "    if odd_number % 2 != 0 and odd_number <= 50 and odd_number >= 1:    \n",
    "        for number in range(1, 50):\n",
    "            if number % 2 != 0 and number == odd_number:\n",
    "                print(\"Yikes! Skipping number: {}\".format(number))\n",
    "            elif number % 2 != 0:\n",
    "                print(\"Here is an odd number: {}\".format(number))                "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "97fdd407",
   "metadata": {},
   "source": [
    " - The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "id": "338a4d85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a positive number: 6\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "posi_numb = int(input(\"Enter a positive number: \"))\n",
    "if posi_numb > 0:\n",
    "    for number in range(0, posi_numb + 1):\n",
    "        print(number)\n",
    "else:\n",
    "    print(\"You did not enter a positive number\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4fed4164",
   "metadata": {},
   "source": [
    " - Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "c57a6db3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a positive number: 5\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "posi_numb = int(input(\"Enter a positive number: \"))\n",
    "while posi_numb >= 1:\n",
    "    print(posi_numb)\n",
    "    posi_numb = posi_numb - 1\n",
    "if posi_numb < 0:\n",
    "    print(\"You did not enter a positive number\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ed9ad2c",
   "metadata": {},
   "source": [
    "### Fizzbuzz\n",
    "\n",
    "One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a7f2a578",
   "metadata": {},
   "source": [
    " - Write a program that prints the numbers from 1 to 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "9f90beda",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n",
      "16\n",
      "17\n",
      "18\n",
      "19\n",
      "20\n",
      "21\n",
      "22\n",
      "23\n",
      "24\n",
      "25\n",
      "26\n",
      "27\n",
      "28\n",
      "29\n",
      "30\n",
      "31\n",
      "32\n",
      "33\n",
      "34\n",
      "35\n",
      "36\n",
      "37\n",
      "38\n",
      "39\n",
      "40\n",
      "41\n",
      "42\n",
      "43\n",
      "44\n",
      "45\n",
      "46\n",
      "47\n",
      "48\n",
      "49\n",
      "50\n",
      "51\n",
      "52\n",
      "53\n",
      "54\n",
      "55\n",
      "56\n",
      "57\n",
      "58\n",
      "59\n",
      "60\n",
      "61\n",
      "62\n",
      "63\n",
      "64\n",
      "65\n",
      "66\n",
      "67\n",
      "68\n",
      "69\n",
      "70\n",
      "71\n",
      "72\n",
      "73\n",
      "74\n",
      "75\n",
      "76\n",
      "77\n",
      "78\n",
      "79\n",
      "80\n",
      "81\n",
      "82\n",
      "83\n",
      "84\n",
      "85\n",
      "86\n",
      "87\n",
      "88\n",
      "89\n",
      "90\n",
      "91\n",
      "92\n",
      "93\n",
      "94\n",
      "95\n",
      "96\n",
      "97\n",
      "98\n",
      "99\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "counter = 1\n",
    "while counter <= 100:\n",
    "    print(counter)\n",
    "    counter = counter + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b1b317b",
   "metadata": {},
   "source": [
    " - For multiples of three print \"Fizz\" instead of the number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "357a4956",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "Fizz\n",
      "4\n",
      "5\n",
      "Fizz\n",
      "7\n",
      "8\n",
      "Fizz\n",
      "10\n",
      "11\n",
      "Fizz\n",
      "13\n",
      "14\n",
      "Fizz\n",
      "16\n",
      "17\n",
      "Fizz\n",
      "19\n",
      "20\n",
      "Fizz\n",
      "22\n",
      "23\n",
      "Fizz\n",
      "25\n",
      "26\n",
      "Fizz\n",
      "28\n",
      "29\n",
      "Fizz\n",
      "31\n",
      "32\n",
      "Fizz\n",
      "34\n",
      "35\n",
      "Fizz\n",
      "37\n",
      "38\n",
      "Fizz\n",
      "40\n",
      "41\n",
      "Fizz\n",
      "43\n",
      "44\n",
      "Fizz\n",
      "46\n",
      "47\n",
      "Fizz\n",
      "49\n",
      "50\n",
      "Fizz\n",
      "52\n",
      "53\n",
      "Fizz\n",
      "55\n",
      "56\n",
      "Fizz\n",
      "58\n",
      "59\n",
      "Fizz\n",
      "61\n",
      "62\n",
      "Fizz\n",
      "64\n",
      "65\n",
      "Fizz\n",
      "67\n",
      "68\n",
      "Fizz\n",
      "70\n",
      "71\n",
      "Fizz\n",
      "73\n",
      "74\n",
      "Fizz\n",
      "76\n",
      "77\n",
      "Fizz\n",
      "79\n",
      "80\n",
      "Fizz\n",
      "82\n",
      "83\n",
      "Fizz\n",
      "85\n",
      "86\n",
      "Fizz\n",
      "88\n",
      "89\n",
      "Fizz\n",
      "91\n",
      "92\n",
      "Fizz\n",
      "94\n",
      "95\n",
      "Fizz\n",
      "97\n",
      "98\n",
      "Fizz\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "counter = 1\n",
    "while counter <= 100:\n",
    "    if counter % 3 == 0:\n",
    "        print('Fizz')\n",
    "    else:    \n",
    "        print(counter)\n",
    "    counter = counter + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "182d2f70",
   "metadata": {},
   "source": [
    " - For the multiples of five print \"Buzz\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "ce36fde2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "Buzz\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "Buzz\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "Buzz\n",
      "16\n",
      "17\n",
      "18\n",
      "19\n",
      "Buzz\n",
      "21\n",
      "22\n",
      "23\n",
      "24\n",
      "Buzz\n",
      "26\n",
      "27\n",
      "28\n",
      "29\n",
      "Buzz\n",
      "31\n",
      "32\n",
      "33\n",
      "34\n",
      "Buzz\n",
      "36\n",
      "37\n",
      "38\n",
      "39\n",
      "Buzz\n",
      "41\n",
      "42\n",
      "43\n",
      "44\n",
      "Buzz\n",
      "46\n",
      "47\n",
      "48\n",
      "49\n",
      "Buzz\n",
      "51\n",
      "52\n",
      "53\n",
      "54\n",
      "Buzz\n",
      "56\n",
      "57\n",
      "58\n",
      "59\n",
      "Buzz\n",
      "61\n",
      "62\n",
      "63\n",
      "64\n",
      "Buzz\n",
      "66\n",
      "67\n",
      "68\n",
      "69\n",
      "Buzz\n",
      "71\n",
      "72\n",
      "73\n",
      "74\n",
      "Buzz\n",
      "76\n",
      "77\n",
      "78\n",
      "79\n",
      "Buzz\n",
      "81\n",
      "82\n",
      "83\n",
      "84\n",
      "Buzz\n",
      "86\n",
      "87\n",
      "88\n",
      "89\n",
      "Buzz\n",
      "91\n",
      "92\n",
      "93\n",
      "94\n",
      "Buzz\n",
      "96\n",
      "97\n",
      "98\n",
      "99\n",
      "Buzz\n"
     ]
    }
   ],
   "source": [
    "counter = 1\n",
    "while counter <= 100:\n",
    "    if counter % 5 == 0:\n",
    "        print('Buzz')\n",
    "    else:    \n",
    "        print(counter)\n",
    "    counter = counter + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2941d087",
   "metadata": {},
   "source": [
    " - For numbers which are multiples of both three and five print \"FizzBuzz\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "e721ac24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "Fizz\n",
      "4\n",
      "Buzz\n",
      "Fizz\n",
      "7\n",
      "8\n",
      "Fizz\n",
      "Buzz\n",
      "11\n",
      "Fizz\n",
      "13\n",
      "14\n",
      "FizzBuzz\n",
      "16\n",
      "17\n",
      "Fizz\n",
      "19\n",
      "Buzz\n",
      "Fizz\n",
      "22\n",
      "23\n",
      "Fizz\n",
      "Buzz\n",
      "26\n",
      "Fizz\n",
      "28\n",
      "29\n",
      "FizzBuzz\n",
      "31\n",
      "32\n",
      "Fizz\n",
      "34\n",
      "Buzz\n",
      "Fizz\n",
      "37\n",
      "38\n",
      "Fizz\n",
      "Buzz\n",
      "41\n",
      "Fizz\n",
      "43\n",
      "44\n",
      "FizzBuzz\n",
      "46\n",
      "47\n",
      "Fizz\n",
      "49\n",
      "Buzz\n",
      "Fizz\n",
      "52\n",
      "53\n",
      "Fizz\n",
      "Buzz\n",
      "56\n",
      "Fizz\n",
      "58\n",
      "59\n",
      "FizzBuzz\n",
      "61\n",
      "62\n",
      "Fizz\n",
      "64\n",
      "Buzz\n",
      "Fizz\n",
      "67\n",
      "68\n",
      "Fizz\n",
      "Buzz\n",
      "71\n",
      "Fizz\n",
      "73\n",
      "74\n",
      "FizzBuzz\n",
      "76\n",
      "77\n",
      "Fizz\n",
      "79\n",
      "Buzz\n",
      "Fizz\n",
      "82\n",
      "83\n",
      "Fizz\n",
      "Buzz\n",
      "86\n",
      "Fizz\n",
      "88\n",
      "89\n",
      "FizzBuzz\n",
      "91\n",
      "92\n",
      "Fizz\n",
      "94\n",
      "Buzz\n",
      "Fizz\n",
      "97\n",
      "98\n",
      "Fizz\n",
      "Buzz\n"
     ]
    }
   ],
   "source": [
    "counter = 1\n",
    "while counter <= 100:\n",
    "    if counter % 3 == 0 and counter % 5 == 0:\n",
    "        print('FizzBuzz')\n",
    "    elif counter % 3 == 0:\n",
    "        print('Fizz')\n",
    "    elif counter % 5 == 0:\n",
    "        print('Buzz')\n",
    "    else:    \n",
    "        print(counter)\n",
    "    counter = counter + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bcdf77a2",
   "metadata": {},
   "source": [
    "### Display a table of powers\n",
    " - Prompt the user to enter an integer.\n",
    " - Display a table of squares and cubes from 1 to the value entered.\n",
    " - Ask if the user wants to continue.\n",
    " - Assume that the user will enter valid data.\n",
    " - Only continue if the user agrees to."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "c4b58711",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Would you like to get started?(y/n) y\n",
      "What number would you like to go up to? 5\n",
      "  Number    Squared    Cubed\n",
      "--------  ---------  -------\n",
      "       1          1        1\n",
      "       2          4        8\n",
      "       3          9       27\n",
      "       4         16       64\n",
      "       5         25      125\n",
      "Would you like to continue?(y/n) y\n",
      "What number would you like to go up to? 4\n",
      "  Number    Squared    Cubed\n",
      "--------  ---------  -------\n",
      "       1          1        1\n",
      "       2          4        8\n",
      "       3          9       27\n",
      "       4         16       64\n",
      "Would you like to continue?(y/n) y\n",
      "What number would you like to go up to? 3\n",
      "  Number    Squared    Cubed\n",
      "--------  ---------  -------\n",
      "       1          1        1\n",
      "       2          4        8\n",
      "       3          9       27\n",
      "Would you like to continue?(y/n) n\n",
      "See ya!\n"
     ]
    }
   ],
   "source": [
    "from tabulate import tabulate\n",
    "table = []\n",
    "continue_loop = input(\"Would you like to get started?(y/n) \")\n",
    "while continue_loop == 'y':\n",
    "    table_of_powers = int(input(\"What number would you like to go up to? \"))\n",
    "    for number in range(1, table_of_powers + 1):\n",
    "        table.append([number, number ** 2, number * number * number])   \n",
    "    print(tabulate(table, headers = [\"Number\", \"Squared\", \"Cubed\"]))\n",
    "    table = []\n",
    "    continue_loop = input(\"Would you like to continue?(y/n) \")\n",
    "else:\n",
    "    print(\"See ya!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8da4a9f1",
   "metadata": {},
   "source": [
    "### Convert given number grades into letter grades\n",
    " - Prompt the user for a numerical grade from 0 to 100.\n",
    " - Display the corresponding letter grade.\n",
    " - Prompt the user to continue.\n",
    " - Assume that the user will enter valid integers for the grades.\n",
    " - The application should only continue if the user agrees to.\n",
    " - Grade Ranges:\n",
    "\n",
    "  - A : 100 - 88\n",
    "  - B : 87 - 80\n",
    "  - C : 79 - 67\n",
    "  - D : 66 - 60\n",
    "  - F : 59 - 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "c87dc387",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Would you like to know your letter grade?(y/n) y\n",
      "What is your numerical grade? 89\n",
      "Your grade is A\n",
      "Would you like to know your letter grade?(y/n) y\n",
      "What is your numerical grade? 85\n",
      "Your grade is B\n",
      "Would you like to know your letter grade?(y/n) n\n",
      "See ya!\n"
     ]
    }
   ],
   "source": [
    "continue_loop = input(\"Would you like to know your letter grade?(y/n) \")\n",
    "while continue_loop == 'y':\n",
    "    grade = int(input(\"What is your numerical grade? \"))\n",
    "    if grade >= 88:\n",
    "        print(\"Your grade is A\")\n",
    "    elif grade >= 80:\n",
    "        print(\"Your grade is B\")\n",
    "    elif grade >= 67:\n",
    "        print(\"Your grade is C\")\n",
    "    elif grade >= 60:\n",
    "        print(\"Your grade is D\")\n",
    "    else:\n",
    "        print(\"Your grade is F\")\n",
    "    continue_loop = input(\"Would you like to know your letter grade?(y/n) \")\n",
    "else:\n",
    "    print(\"See ya!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d24a9f74",
   "metadata": {},
   "source": [
    "### Bonus\n",
    " - Edit your grade ranges to include pluses and minuses"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "8ebda91c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Would you like to know your letter grade?(y/n) y\n",
      "What is your numerical grade? 95\n",
      "Your grade is A\n",
      "Would you like to know your letter grade?(y/n) y\n",
      "What is your numerical grade? 99\n",
      "Your grade is A+\n",
      "Would you like to know your letter grade?(y/n) n\n",
      "See ya!\n"
     ]
    }
   ],
   "source": [
    "continue_loop = input(\"Would you like to know your letter grade?(y/n) \")\n",
    "while continue_loop == 'y':\n",
    "    grade = int(input(\"What is your numerical grade? \"))\n",
    "    if grade >= 97:\n",
    "        print(\"Your grade is A+\")\n",
    "    elif grade >= 94:\n",
    "        print(\"Your grade is A\")        \n",
    "    elif grade >= 90:\n",
    "        print(\"Your grade is A-\")\n",
    "    elif grade >= 87:\n",
    "        print(\"Your grade is B+\")        \n",
    "    elif grade >= 84:\n",
    "        print(\"Your grade is B\")\n",
    "    elif grade >= 80:\n",
    "        print(\"Your grade is B-\")\n",
    "    elif grade >= 77:\n",
    "        print(\"Your grade is C+\")\n",
    "    elif grade >= 74:\n",
    "        print(\"Your grade is C\")\n",
    "    elif grade >= 70:\n",
    "        print(\"Your grade is C-\")        \n",
    "    elif grade >= 67:\n",
    "        print(\"Your grade is D+\")\n",
    "    elif grade >= 64:\n",
    "        print(\"Your grade is D\")\n",
    "    elif grade >= 60:\n",
    "        print(\"Your grade is D-\")\n",
    "    else:\n",
    "        print(\"Your grade is F\")\n",
    "    continue_loop = input(\"Would you like to know your letter grade?(y/n) \")\n",
    "else:\n",
    "    print(\"See ya!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2266119",
   "metadata": {},
   "source": [
    "### Create a list of dictionaries\n",
    " - Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.\n",
    "  - Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "86e0b91d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'title': 'The Alchemist', 'author': 'Paulo Coelho', 'genre': 'Fiction'}, {'title': 'The Undocumented Americans', 'author': 'Karla Villavicencio', 'genre': 'Non-Fiction'}, {'title': 'Slaughterhouse-five', 'author': 'Kurt Vonnegut Jr.', 'genre': 'Sci-Fi'}, {'title': 'Maus', 'author': 'Art Spiegelman', 'genre': 'Graphic Novel'}]\n"
     ]
    }
   ],
   "source": [
    "book_list = [\n",
    "    {'title':'The Alchemist', 'author':'Paulo Coelho', 'genre':'Fiction'},\n",
    "    {'title':'The Undocumented Americans', 'author':'Karla Villavicencio', 'genre':'Non-Fiction'},\n",
    "    {'title':'Slaughterhouse-five', 'author':'Kurt Vonnegut Jr.', 'genre':'Sci-Fi'},\n",
    "    {'title': 'Maus', 'author':'Art Spiegelman', 'genre':'Graphic Novel'}\n",
    "]\n",
    "print(book_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "1488151a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The book title is: The Alchemist. The book author is: Paulo Coelho. The book genre is: Fiction\n",
      "The book title is: The Undocumented Americans. The book author is: Karla Villavicencio. The book genre is: Non-Fiction\n",
      "The book title is: Slaughterhouse-five. The book author is: Kurt Vonnegut Jr.. The book genre is: Sci-Fi\n",
      "The book title is: Maus. The book author is: Art Spiegelman. The book genre is: Graphic Novel\n"
     ]
    }
   ],
   "source": [
    "for book in book_list:\n",
    "    print(f\"The book title is: {book['title']}. The book author is: {book['author']}. The book genre is: {book['genre']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "ba8ff1d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a book genre: Fiction\n",
      "{'title': 'The Alchemist', 'author': 'Paulo Coelho', 'genre': 'Fiction'}\n"
     ]
    }
   ],
   "source": [
    "genre_input = input(\"Enter a book genre: \")\n",
    "for book in book_list:\n",
    "    if genre_input == book['genre']:\n",
    "        print(book)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "881a9d48",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
