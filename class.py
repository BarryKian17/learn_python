class Car():
    sterring = 6
    def __init__(self,name,wheel):
        self.name = name
        self.wheel = wheel
    
    def drive(self):
        print(f'{self.name} with {self.wheel} wheels is driving ste{self.sterring}')
    
    @classmethod 
    def common(cls):
        print(f"all car has only {cls.sterring}")

list = Car("mercede0",4)
list.drive()

bmw = Car("bmw" , 5)
bmw.drive()

bmw.common()
Car.common()