
#illustrating polymorphism in python
class Cat:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def information(self):
        print(f'{self.name} is {self.age} years old')  
    def makeSound(self):
        print('meow')     
class Dog:
    def __init__(self,name, age): 
        self.name = name
        self.age = age  
    def information(self):
        print(f'{self.name} is {self.age} years old')  
    def makeSound(self):
        print('woof')  

cat1=Dog('sibwor', 20)
dog1=Cat('swiss',10)
'''
method informaion and make sound is being used in two different forms each

'''
cat1.information()
dog1.information()
dog1.makeSound()
cat1.makeSound()
          
