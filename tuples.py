#!/usr/bin/env python

#tuple is immutable- use parenthesis to declare it
tuple1=('Githeri','chips', 'mursik', 'ugali','pizza')
print(type(tuple1))
print(tuple1)

for items in tuple1:
    print(items)

#add elements to tuple
add_food = ('chapoo',)
tuple1 +=add_food
print (tuple1)

#add and del elements in tuple
tuple1 = list(tuple1)
tuple1.append("rice")
tuple1.remove('chips')
tuple1 = tuple(tuple1)

print(tuple1)

#tuple lenght
print(f" The length of this tuple is {len (tuple1)}")
