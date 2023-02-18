class  rectangle:
    def __init__(self, length, width ):
        self.length = length
        self.width = width
# area calculation
    def area(self):
        area = self.length*self.width
        print("\nThe area is ",area)
    def perimeter(self):
        perimeter = self.width + self.length
        print("\nThe perimeter is ",perimeter)

length = int(input("\nEnter  Length: "))
width = int(input("\nEnter  Width: "))
# conclusion
a = rectangle(length,width)
a.area()
a.perimeter()
