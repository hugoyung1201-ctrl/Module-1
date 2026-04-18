class Parrot:
    spieces = "bird"
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def singing(self):
        print("{} is singing songs".format(self.name))
blu = Parrot('blu',10)
connor = Parrot('connor',15)
print(blu.spieces)
print(connor.spieces)
print(blu.name)
print(connor.name)
print(blu.age)
print(connor.age)
blu.singing()
connor.singing()