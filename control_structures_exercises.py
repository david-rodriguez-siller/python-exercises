{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ed74bb6a",
   "metadata": {},
   "source": [
    "### Conditional Basics"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a44f560",
   "metadata": {},
   "source": [
    "#### a. prompt the user for a day fo the week, print out whether the day is Monday or not"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b5b93fee",
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
   "id": "fe992c9b",
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
   "id": "374735ee",
   "metadata": {},
   "source": [
    "#### b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5ac401d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_it_the_weekend():\n",
    "    weekday = input(\"Enter the day of the week: \")\n",
    "    if weekday.lower() == 'saturday' or weekday.lower() == 'sunday':\n",
    "        print(\"Today is {}! Happy beginning of the week!\".format(weekday.capitalize()))\n",
    "    else:\n",
    "        print(\"Today is {}. It is not the weeked. :( \".format((weekday.capitalize())))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "4c2483d1",
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
   "id": "c1e94657",
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
   "execution_count": 26,
   "id": "45344fb0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How many hours did you work last week? 40\n",
      "What is your hourly rate? 25\n",
      "Your weekly wages are: $1000\n"
     ]
    }
   ],
   "source": [
    "hours_worked = int(input(\"How many hours did you work last week? \"))\n",
    "hourly_rate = int(input(\"What is your hourly rate? \"))\n",
    "weekly_wages = print(\"Your weekly wages are: ${}\".format(hours_worked * hourly_rate))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b52dc2d8",
   "metadata": {},
   "source": [
    "### Loop Basics"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b15563fb",
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
   "execution_count": 27,
   "id": "874d3ff0",
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
      "15\n",
      "16\n"
     ]
    }
   ],
   "source": [
    "i = 5\n",
    "while i <= 15:\n",
    "    i = i + 1\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b260cd2",
   "metadata": {},
   "source": [
    " - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.\n",
    " - Alter your loop to count backwards by 5's from 100 to -10.\n",
    " - Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c655c323",
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
   "cell_type": "code",
   "execution_count": 32,
   "id": "d71e860c",
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
   "cell_type": "code",
   "execution_count": 33,
   "id": "559e0e85",
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
   "id": "3dee549c",
   "metadata": {},
   "source": [
    " - Write a loop that uses print to decrease from value 100 to 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "c9d4fd9c",
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
   "id": "cfeb558a",
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
   "id": "36798cf4",
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
   "id": "cfe3f9a7",
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
   "id": "15753609",
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
   "id": "fdafb53b",
   "metadata": {},
   "source": [
    "###  Break and Continue"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4509e9c9",
   "metadata": {},
   "source": [
    " - Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "d8ae4644",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number to skip is: 9\n",
      "Here is an odd number: 1\n",
      "Here is an odd number: 3\n",
      "Here is an odd number: 5\n",
      "Here is an odd number: 7\n",
      "Yikes! Skipping number: 9\n",
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
    "odd_number = int(input(\"Number to skip is: \"))\n",
    "if odd_number % 2 != 0 and odd_number <= 50 and odd_number >= 1:    \n",
    "    for number in range(1, 50):\n",
    "        if number % 2 != 0 and number == odd_number:\n",
    "            print(\"Yikes! Skipping number: {}\".format(number))\n",
    "        elif number % 2 != 0:\n",
    "            print(\"Here is an odd number: {}\".format(number))\n",
    "else:\n",
    "    print(\"You did not enter an odd number between 1 and 50\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a9ec9de",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba916071",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1e9c8d1",
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
