#!/usr/bin/env python

#dict keys and values
thisdict ={
'brand': 'ford',
'model': 'mustang',
'year': 1964
}
print(thisdict.keys())
print(thisdict.values())

'''
dict iteration
'''
print("\n")
for key, value in thisdict.items():
    print(f'{key} is {value}')
print('\n')

#accessing dict values 
print(thisdict.get('year'))
print(thisdict.get('model'))

#delete method use del statement

del thisdict['year']
print(thisdict)


