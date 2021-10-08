{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ed21a311",
   "metadata": {},
   "source": [
    "### 20 Python Data Structure Manipulation Exercises"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2a32c4d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "students = [\n",
    "    {\n",
    "        \"id\": \"100001\",\n",
    "        \"student\": \"Ada Lovelace\",\n",
    "        \"coffee_preference\": \"light\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [70, 91, 82, 71],\n",
    "        \"pets\": [{\"species\": \"horse\", \"age\": 8}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100002\",\n",
    "        \"student\": \"Thomas Bayes\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [75, 73, 86, 100],\n",
    "        \"pets\": [],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100003\",\n",
    "        \"student\": \"Marie Curie\",\n",
    "        \"coffee_preference\": \"light\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [70, 89, 69, 65],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 0}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100004\",\n",
    "        \"student\": \"Grace Hopper\",\n",
    "        \"coffee_preference\": \"dark\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [73, 66, 83, 92],\n",
    "        \"pets\": [{\"species\": \"dog\", \"age\": 4}, {\"species\": \"cat\", \"age\": 4}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100005\",\n",
    "        \"student\": \"Alan Turing\",\n",
    "        \"coffee_preference\": \"dark\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [78, 98, 85, 65],\n",
    "        \"pets\": [\n",
    "            {\"species\": \"horse\", \"age\": 6},\n",
    "            {\"species\": \"horse\", \"age\": 7},\n",
    "            {\"species\": \"dog\", \"age\": 5},\n",
    "        ],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100006\",\n",
    "        \"student\": \"Rosalind Franklin\",\n",
    "        \"coffee_preference\": \"dark\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [76, 70, 96, 81],\n",
    "        \"pets\": [],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100007\",\n",
    "        \"student\": \"Elizabeth Blackwell\",\n",
    "        \"coffee_preference\": \"dark\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [69, 94, 89, 86],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 10}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100008\",\n",
    "        \"student\": \"Rene Descartes\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [87, 79, 90, 99],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 10}, {\"species\": \"cat\", \"age\": 8}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100009\",\n",
    "        \"student\": \"Ahmed Zewail\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [74, 99, 93, 89],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 0}, {\"species\": \"cat\", \"age\": 0}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100010\",\n",
    "        \"student\": \"Chien-Shiung Wu\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [82, 92, 91, 65],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 8}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100011\",\n",
    "        \"student\": \"William Sanford Nye\",\n",
    "        \"coffee_preference\": \"dark\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [70, 92, 65, 99],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 8}, {\"species\": \"cat\", \"age\": 5}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100012\",\n",
    "        \"student\": \"Carl Sagan\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [100, 86, 91, 87],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 10}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100013\",\n",
    "        \"student\": \"Jane Goodall\",\n",
    "        \"coffee_preference\": \"light\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [80, 70, 68, 98],\n",
    "        \"pets\": [{\"species\": \"horse\", \"age\": 4}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100014\",\n",
    "        \"student\": \"Richard Feynman\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [73, 99, 86, 98],\n",
    "        \"pets\": [{\"species\": \"dog\", \"age\": 6}],\n",
    "    },\n",
    "]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c26cb638",
   "metadata": {},
   "source": [
    "- How many students are there?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5a084ca",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "9893c740",
   "metadata": {},
   "source": [
    "- How many students prefer light coffee? For each type of coffee roast?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "befa30d4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "c7e4d90b",
   "metadata": {},
   "source": [
    "- How many types of each pet are there?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c91206f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "fe988014",
   "metadata": {},
   "source": [
    "- How many grades does each student have? Do they all have the same number of grades?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b2b16de",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "91c7dfa5",
   "metadata": {},
   "source": [
    "- What is each student's grade average?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b4349e2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "bfe73507",
   "metadata": {},
   "source": [
    "- How many pets does each student have?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5fa2a1a6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "a8188442",
   "metadata": {},
   "source": [
    "- How many students are in web development? data science?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8f24ef4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "7df7c018",
   "metadata": {},
   "source": [
    "- What is the average number of pets for students in web development?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b88fa224",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "990b6fae",
   "metadata": {},
   "source": [
    "- What is the average pet age for students in data science?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b86305f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "b8410707",
   "metadata": {},
   "source": [
    "- What is most frequent coffee preference for data science students?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c039dab",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "e3b64020",
   "metadata": {},
   "source": [
    "- What is the least frequent coffee preference for web development students?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8cc4bf08",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "1b17912b",
   "metadata": {},
   "source": [
    "- What is the average grade for students with at least 2 pets?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17e87406",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "f6d3e207",
   "metadata": {},
   "source": [
    "- How many students have 3 pets?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8788499b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "67881e46",
   "metadata": {},
   "source": [
    "- What is the average grade for students with 0 pets?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2152892b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "233f02b7",
   "metadata": {},
   "source": [
    "- What is the average grade for web development students? data science students?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09e3e958",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "a1da7b4b",
   "metadata": {},
   "source": [
    "- What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "883c1fd0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "131f6768",
   "metadata": {},
   "source": [
    "- What is the average number of pets for medium coffee drinkers?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa1efcee",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "3eb6bca7",
   "metadata": {},
   "source": [
    "- What is the most common type of pet for web development students?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cba6d58",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "68ced731",
   "metadata": {},
   "source": [
    "- What is the average name length?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39cbcf99",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "44d9f800",
   "metadata": {},
   "source": [
    "- What is the highest pet age for light coffee drinkers?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5226d2cc",
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
