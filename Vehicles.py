# class vehicle
class Vehicles_Class:
    # Constructor which helps to initiate new object
    def __init__(self, brand, model, type):
        # below are the attributes
        self.brand = brand
        self.model = model
        self.type = type
        self.fuel_tank = 30
        self.fuel_level = 0
    
    # Methods / function
    def check_fuel(self):
        self.fuel_level = self.fuel_tank
        print('Fuel tank is full')

    def drive(self):
        print(f'The {self.model} is now driving')

    # update an attribute’s value
    def update_fuel_level(self,current_level):
        if current_level <= self.fuel_tank:
            self.fuel_level = current_level
        else:
            print('NA')

    # method to increment an attribute’s value
    def get_fuel(self, amount):
        if (self.fuel_level + amount <= self.fuel_tank):
            self.fuel_level += amount
            print('Added fuel.')
        else:
            print('The tank wont hold that much.')