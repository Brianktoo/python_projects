
class Vehicle():
     def __init__(self, model, year, color, price ):
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        print(f"properties: {self.model} {self.year} {self.price} {self.color} ")

     def direction(self):
        if self.model == 'V8' or self.model == 'Brado' or self.model == 'Mercedes benz':
            print('Go forward,.. welcome to VIP entrance!')
        else:
            print('Go backward,.. not allowed here!, use regular route')   

     def maxspeed(self):
         print('Max speed is 100km/hr')
                 
    
 
v2=Vehicle('V8', 2001, 'brown', '7.5M') 
v3=Vehicle('Probox', 2001, 'brown', '0.8M') 
v4=Vehicle('Toyota', 2001, 'brown', '7.5M')
v5=Vehicle('Brado', 2001, 'brown', '7.5M')

v2.direction()
v3.direction()
v4.direction()
v5.direction()
v2.maxspeed()
    #inheritances from class Vehicle
class Motorcycle(Vehicle):
    def __init__(self, model, year, color, price, speed):
         super().__init__(model, year, color, price)
         self.speed = speed
         print(f"properties: {self.model} {self.year} {self.price} {self.color} {self.speed}")

         #overide a method in base class
    def maxspeed(self):
        print('Max speed is 50km/hr')     

m1=Motorcycle('TVS','2019','black','200k','10km/hr')  
m1.direction()  
m1.maxspeed() 

