#!/usr/bin/env python

names = ['brian', 'amon','mesh', 'jacob', 'too', 'mercy','cherop', 'ian']
alphabets =['d', 'a', 'c', 'b', 'e', 'g', 'k', 'l']
print(f'name lists not sorted {names}')
names.sort()
print(f'sorted names list {names}'
      )
print(f'list of alphabets that has not been sorted {alphabets}')

alphabets.sort(reverse=True)
print(f'list of alphabets in reverse order {alphabets}')

print(f'The lenght of alphabet list is {len(alphabets)}')

#looping- For loop
for n in names:
    print(f'My name is {n.title()}')

#iterating over a string
specialization='developer'
print (f'iterating over string {specialization}')
for x in specialization:
    print(x)

#range
for i in range(5):
      print(i)

for i in range(10,20):
      print (i)
