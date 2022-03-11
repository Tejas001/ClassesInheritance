from PractiseClass.Battery import Battery
from PractiseClass.Vehicles import Vehicles_Class

# Child class (Inheritance)
class Electric_vehicle(Vehicles_Class,Battery):

    def __init__(self, brand, model, type):
        super().__init__(brand, model, type)
        self.battery = Battery()
        
    # Over-riding parent methods
    def check_fuel(self):
        print('This class has no fuel tank')

    def charge(self):
        self.charge_level = 100
        print('The vehicle is now charged full')


