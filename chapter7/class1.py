class Car:
    def __init__(self, color,speed):
        self.color=color
        self.speed=speed

    def speedUp(self, v):
        self.speed = self.speed + v
        return self.speed

    def speedDown(self,v):
        self.speed=self.speed-v
        return self.speed

mycar = Car('Black', 60)
print('색상:', mycar.color, '속도:', mycar.speed)
mycar.color="Red"
print("색상:", mycar.color)
mycar.speedUp(10)
print("속도:", mycar.speed)
mycar.speedDown(20)
print("속도:", mycar.speed)