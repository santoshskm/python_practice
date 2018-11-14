class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display(self):
        print("length:",self.length)
        print("width:",self.width)
        print("Area:",self.length*self.width)

obj=Rectangle(4,5)
obj.display()