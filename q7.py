""" Solution for Question 7 """

""" 
- defining a class named Car with attributes: make, model, year 
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make # Attribute: make
        self.model = model # Attribute: model
        self.year = year # Attribute: year

    def describe_car(self):
        print("Car Attributes - Year:{} Make:{} Model:{}".format(self.year, self.make, self.model))


my_car = Car("Toyota", "Corolla", 2020)
my_car.describe_car()
