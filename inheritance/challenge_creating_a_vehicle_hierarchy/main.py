class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        pass
    
    def get_info(self):
        return f" Brand: {self.brand}, Speed: {self.speed}"
        pass

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand,speed)
        self.doors = doors
        pass
    
    def get_info(self):
        return f"{super().get_info()}, Doors: {self.doors}"
        pass

class Bike(Vehicle):
    def __init__(self, brand, speed, type):
        super().__init__(brand,speed)
        self.type = type
        pass
    
    def get_info(self):
        return f"{super().get_info()}, Type: {self.type}"
        pass

# Create one object of each class and print their information
v = Vehicle('Generic', 50)
c = Car('Toyota', 120, 4)
b = Bike('Giant', 30, 'mountain')

print(v.get_info())
print(c.get_info())
print(b.get_info())