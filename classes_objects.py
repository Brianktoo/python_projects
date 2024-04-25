
class Car:
    def __init__(self, model, color, price, year):
        self.model = model
        self.year = year
        self.color = color
        self.price = price
    
    def car_info(self):
        print(f"Car: {self.year} {self.model} {self.price} {self.color}")

# Creating objects of the Car class
car1 = Car("Toyota", 2020, 'white', '2M')
car2 = Car("Honda", 2019, 'red', '1.5M')
car3 = Car("Brado", 2019, 'red', '3.5M')
car4 = Car("V8", 2018, 'black', '4.5M')


# Calling methods
car1.car_info()  
car2.car_info()
car3.car_info()
car4.car_info()  
