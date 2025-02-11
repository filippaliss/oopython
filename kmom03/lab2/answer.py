#!/usr/bin/env python3

"""
0b594bab4ad34d09335d3275efdbad6a
oopython
lab2
v2
fili22
2025-01-26 14:16:13
v4.0.0 (2019-03-05)

Generated 2025-02-01 11:45:03 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()

from classes import Person, Address



# ==========================================================================
# Lab 2 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.  
#



# --------------------------------------------------------------------------
# Section 1. Class relationships
#
# Practice on creating classes and relationships between them in python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (2 points)
#
# Create a new file, put your code for the classes in it, call it
# **classes.py**.
#
# Create a new class named **Person**.  Give the class the instance
# attributes "name" and "ssn". Make "ssn" a private attribute. The values for
# the attributes should be sent to the constructor as arguments.
# Create a *get* property for "ssn".
#
# In the code below create a new variable called **per** and set it to a new
# instance of Person. Give it the name `FitzChivalry` and ssn `350967-5218`.
#
#
# Answer with per\'s getter for ssn.
#
# Write your code below and put the answer into the variable ANSWER.
#


per = Person("FitzChivalry", "350967-5218")



ANSWER = per.ssn

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (2 points)
#
# Create a new class named **Address**.  Give the class the instance
# attributes "city", "state" and "country". The values for the attributes
# should be sent to the constructor as arguments.
# Create the magic method **_\_str_\_**, in Address, it should return
# `"Address: <city> <state> <country>"` (replace the \<city\> with the value
# of the attribute city...).
#
# Create a new instance of the class Address. Initiate it with the city
# `Buckkeep`, the state `Gotland` and the country `Andor` and store it in a
# variable called **per_address**.
#
# Now, go back and add the instance attribute **address** to your Person
# class. It's value should be sent as argument to constructor, give it a
# default value of and empty string, `""`.
# Create a set method for the attribute "address".
#
# Create the magic method **_\_str_\_** for Person, it should return `"Name:
# <name> SSN: <ssn> Address: <city> <state> <country>"` if the person has an
# address or, `"Name: <name> SSN: <ssn>"` if its an empty string.
#
# Use Address' string representation to get address the data.
#
# Use the set method in Person to add the newly create Address object to your
# **per** object.
#
# Answer with per's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#

per_address = Address("Buckkeep", "Gotland", "Andor")

per.set_address(per_address)


ANSWER = str(per)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (2 points)
#
# Create a new class name **Teacher** make it inherit from class "Person".
# Add the instance attribute "courses" and initiate it to and empty list.
# Create the method **add_course**, it should take one argument and add it to
# the course list attribute.
# Overload the `__str__` method from the base class. It should return the
# same as the original method and add the courses to the end of the string,
# `"Name: <name> SSN: <ssn> Address: <city> <state> <country> Courses:
# <course>, <course>, ..."`. The list of courses should be comma seperated
# without one at the end. Use `super()` to access base method.
#
#
# Create a new instance of the class Teacher. Initiate it with the name
# `Goliat` and ssn `228474-2825`.
# Use the add_course method to add the following courses, `htmlphp`, `webapp`
# and `ramverk2`.
#
#
# Answer with the Teacher object's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (2 points)
#
# Create a new class name **Student** make it inherit from class "Person".
# Add the instance attribute "courses_grades" and initiate it to and empty
# list.
# Create the method **add_course_grade**, it should take two arguments, one
# course and a grade. Create a tuple with the two arguments and add to the
# attribute "courses_grades".
# Create the method **average_grade**. Calculate and return the students
# average grade. Ignore grades with "-" in the calculation.
#
# Create a new instance of the class Student. Initiate it with the name
# `James` and ssn `768244-4857`.
# Use the add_course_grade method to add the following courses, `oopython`
# with grade `4`, `htmlphp` with grade `-` and `webgl` with grade `3`.
#
#
# Answer with the Student object's "average_grade" method.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)


dbwebb.exit_with_summary()
