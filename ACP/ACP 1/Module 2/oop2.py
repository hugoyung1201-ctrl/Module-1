class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def rectangle_area(self):
        return self.length*self.width
r1 = rectangle(10,15)  
print("Area of Rectangle is ", r1.rectangle_area())