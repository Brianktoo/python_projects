#!/usr/bin/env python
dict = {1:'brian', 2:'kipkosgei', 3:['25 years old']}

print(dict)
#accessing keys of a dictionary
print(dict[1])
print(dict[2])
print(dict[3])

# creating a dictionary
country_capital ={
    'usa': 'washington',
    'india': 'new delhi',
    'japan': 'tokyo',
    'australia': 'canberra',
    'brazil': 'brasilia',
    'kenya': 'nairobi',
    'russia': 'moscow',
    'china': 'beijing'
}
#accessing dictionary items
print(f'capital city of USA is {country_capital['usa']}')
print(f'capital city of India is {country_capital["india"]}')
print(f'capital city of Japan is {country_capital["japan"]}')
print(f'capital city of Australia is {country_capital["australia"]}')

#add items an dict
country_capital['canada'] = 'ottawa'
country_capital['Ethiopia'] = 'Addis Ababa'
print(f'\n{country_capital}')

#deleting items in dictionary by key
del country_capital['usa']
del country_capital['india']

print(f'\n{country_capital}')

#deleting items in dictionary by value
country_capital.pop('canada')
country_capital.pop('Ethiopia')
print(f'\n{country_capital}')

#iterating over a dictionary
for key, value in country_capital.items():
    print(f'capital city of {key} is {value}')

# accesing specific keys
for keys in country_capital.keys():
    print(f'{keys} is a Country')
 #accesing specific values
for values in country_capital.values():
    print(f'{values} is a capital city in a certain country in Africa')


    #changing dictionary items
country_capital['kenya'] = 'xxx'
country_capital['japan'] = 'xxyy'
print(f'\n{country_capital}')

#get dict lenght
print(f'\nThe lenght of this dictionary is {len(country_capital)}')
 #deleting all items in a dictionary
country_capital.clear()
print(f'\n{country_capital}')   
print(f'\n the lenght of dict is {len(country_capital)}')

#insert items to dictionary
country_capital['usa'] = 'washington'
country_capital['india'] = 'new delhi'
print(country_capital)

#dictionary membership test
print('usa' in country_capital)
print('uganda' in country_capital)


