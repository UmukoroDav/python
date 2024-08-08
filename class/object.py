class Car:
    def __init__(self, name, year, model):
        self.name = name    
        self.year = year
        self.model = model
        
    def Motor(self):
        print('The name of my car is', self.name, 'it was made in the year', self.year, 'and the model is', self.model)
        
demo_car = Car('Camrey', 2005, 'Toyota')
demo_car2 = Car('Benz', 2005, 'Toyota')
print(demo_car)
print(demo_car2)
demo_car.Motor()
demo_car2.Motor()