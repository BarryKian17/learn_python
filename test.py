from Car.car import Car
from Car.function import engine

list = Car("mercede0",4)
list.drive()
print(list.sterring)

bmw = Car("bmw" , 5)
bmw.drive()

bmw.common()
Car.common()

engine()