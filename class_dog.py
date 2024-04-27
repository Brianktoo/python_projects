
class Dog():
    def __init__(self, name, age, color): # Dog attributes
        self.name = name
        self.age = age
        self.color = color
    def properties(self, name, age, color):
        print(f'my pet is called {name},it is {age} and its color is  {color}')   

    def Speak(self):
        print('bark') 
dog1=Dog('name', 'age', 'color') 
dog1.Speak()
dog1.properties('simba',12 , 'grey') 
     
#class Cat inheriting from class Dog
class Cat(Dog):
    def __init__(self,name, age, color):
        pass # use when you dont want to add other properties or methods
        #super().__init__(name, age, color)
cat1=Cat('grey_cat1', 25 , 'black') 
cat1.properties('grey_cat1', 25 , 'black')
cat1.Speak()  

# class person inheriting from class Dog
class Person(Dog):
    def __init__(self,name,age, color, gender, country):
        super().__init__(name, age, color) # allows you to add other properties and methods to  new class
        self.gender = gender
        self.country = country
    def speak(self):
        print('hello')   
    def person_discriptions(self,name,age, color,gender, country):
        print(f'{name} {age} {color}{gender}{country}')     
p1= Person('name', 'age', 'color', 'country', 'gender')
p1.speak()  
p1.person_discriptions('brian kipkosgei,', '25 years old,', 'black_chocholate,', ' male,', ' USA')      
    
        
           
       
