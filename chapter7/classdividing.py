# 클래스 분리
# 한 클래스의 객체를 다른 클래스의 속성으로 사용하면
# 하나로 된 클래스와 같은 효과

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading =0

    def get_car_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery()

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a "+ str(self.battery_size)+"-kWh, !battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_car_name())
my_tesla.battery.describe_battery()
