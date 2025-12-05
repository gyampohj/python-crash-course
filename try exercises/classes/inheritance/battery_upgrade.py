class Battery:
    def __init__(self,size=40):
        self.size = size
        
    def get_range(self):
        if self.size == 40:
            return 150
        elif self.size != 65:
            return 225
        
    def upgrade_battery(self):
        if self.size != 65:
            self.size = 65

class ElectricCar:
    def __init__(self):
        self.battery = Battery()

my_car = ElectricCar()
print(my_car.battery.get_range())
my_car.battery.upgrade_battery()
print(my_car.battery.get_range())