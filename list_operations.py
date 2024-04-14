#!/usr/bin/env python

numbers = [10, 50, 20, 40, 30]
print(numbers[0:5])

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(f"The lenght of list numbers is {len(numbers)}")

sum = sum(numbers)
print(f"The sum of all items in the list is {sum}")

color_list =['Red', 'Green', 'White', 'Black']
first_el = color_list[0]
last_el = color_list[-1]
print(f"The first element is {first_el} and the last element is {last_el}")
