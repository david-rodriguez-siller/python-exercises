{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c07b1a13",
   "metadata": {},
   "source": [
    "# 17 list comprehension problems in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4715cc82",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']\n",
    "\n",
    "numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57d8e3c2",
   "metadata": {},
   "source": [
    "### Example for loop solution to add 1 to each number in the list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "42bedc0b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 18, 20, 24, 257, -7, -3, -1, 6, -8]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numbers_plus_one = []\n",
    "for number in numbers:\n",
    "    numbers_plus_one.append(number + 1)\n",
    " \n",
    "numbers_plus_one"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9929330",
   "metadata": {},
   "source": [
    "### Example of using a list comprehension to create a list of the numbers plus one."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "bcf7e477",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 18, 20, 24, 257, -7, -3, -1, 6, -8]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numbers_plus_one = [number + 1 for number in numbers]\n",
    "\n",
    "numbers_plus_one"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5894a0f2",
   "metadata": {},
   "source": [
    "### Example code that creates a list of all of the list of strings in fruits and uppercases every string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "426bc6ff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['MANGO', 'KIWI', 'STRAWBERRY', 'GUAVA', 'PINEAPPLE', 'MANDARIN ORANGE']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "output = []\n",
    "for fruit in fruits:\n",
    "    output.append(fruit.upper())\n",
    "    \n",
    "output    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cfcf082d",
   "metadata": {},
   "source": [
    "#### Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "400d1f69",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['MANGO', 'KIWI', 'STRAWBERRY', 'GUAVA', 'PINEAPPLE', 'MANDARIN ORANGE']"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uppercased_fruits = []\n",
    "\n",
    "for fruit in fruits:\n",
    "    uppercased_fruits.append(fruit.upper())\n",
    "\n",
    "uppercased_fruits"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a39ba71f",
   "metadata": {},
   "source": [
    "#### Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1e1c5ab5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Mango', 'Kiwi', 'Strawberry', 'Guava', 'Pineapple', 'Mandarin orange']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "capitalized_fruits = []\n",
    "\n",
    "for fruit in fruits:\n",
    "    capitalized_fruits.append(fruit.capitalize())\n",
    "    \n",
    "capitalized_fruits"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a4ad9763",
   "metadata": {},
   "source": [
    "#### Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9712bf7",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruits_with_more_than_two_vowels\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cbfb55a9",
   "metadata": {},
   "source": [
    "#### Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f661f6ec",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "e832ae10",
   "metadata": {},
   "source": [
    "#### Exercise 5 - make a list that contains each fruit with more than 5 characters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9a47bfa7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['strawberry', 'pineapple', 'mandarin orange']"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[fruit for fruit in fruits if len(fruit) > 5]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3f2f84d",
   "metadata": {},
   "source": [
    "#### Exercise 6 - make a list that contains each fruit with exactly 5 characters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "cd34609c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['mango', 'guava']"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[fruit for fruit in fruits if len(fruit) == 5]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c06bee20",
   "metadata": {},
   "source": [
    "#### Exercise 7 - Make a list that contains fruits that have less than 5 characters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "035c5f4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['kiwi']"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[fruit for fruit in fruits if len(fruit) < 5]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e373517",
   "metadata": {},
   "source": [
    "#### Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "39fbd10c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 4, 10, 5, 9, 15]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_length = [len(fruit) for fruit in fruits]\n",
    "\n",
    "fruit_length"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "53b2c887",
   "metadata": {},
   "source": [
    "#### Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter \"a\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54f9a179",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "1c2df910",
   "metadata": {},
   "source": [
    "#### Exercise 10 - Make a variable named even_numbers that holds only the even numbers "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55347371",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "95ee2461",
   "metadata": {},
   "source": [
    "#### Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a08ef465",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "66ff6752",
   "metadata": {},
   "source": [
    "#### Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "5113ba1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, 5]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "positive_numbers = []\n",
    "\n",
    "for number in numbers:\n",
    "        if number > 0:\n",
    "            positive_numbers.append(number)\n",
    "            \n",
    "positive_numbers"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "50602ddf",
   "metadata": {},
   "source": [
    "#### Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "34d16bb5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-8, -4, -2, -9]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "negative_numbers = []\n",
    "\n",
    "for number in numbers:\n",
    "        if number < 0:\n",
    "            negative_numbers.append(number)\n",
    "            \n",
    "negative_numbers"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e5fdb231",
   "metadata": {},
   "source": [
    "#### Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "deedbcc2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "665ccb77",
   "metadata": {},
   "source": [
    "##### Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6196b16",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "4163843c",
   "metadata": {},
   "source": [
    "#### Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88a499f8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "12ef2a7a",
   "metadata": {},
   "source": [
    "#### Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55ff1cca",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "9baebb8a",
   "metadata": {},
   "source": [
    "#### BONUS Make a variable named \"primes\" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "961daf2c",
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
