#!/usr/bin/env python3
"""
Contains the Car class.
"""
import random # nytt

random.seed("car")
print("First number: ", random.randint(1, 100))
print("Second number: ", random.randint(1, 100))

class Car():
    """ Car class that handles cars with model and price. """
    wheels = 4

    def __init__(self, model, price):
        """ Constuctor """
        self.model = model
        self.price = price
        self.vin_nr = random.randint(100,999) # nytt

    def present_car(self):
        """ Returns a string presenting the car """
        return "This car is of model {m} and costs {p}$.".format(
            m=self.model, p=self.price)