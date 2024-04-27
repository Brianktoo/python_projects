#!/usr/bin/env python

class Expenses(object):
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
        
    def meth(self):
        ...
    def __add__(self, other):
             return self.cost + other.cost 
food=Expenses('rice', 150)
fuel= Expenses('petrol', 180)
print(food + fuel)
     

