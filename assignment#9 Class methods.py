class  rectangle:
    def __init__(self, area_length, area_width, perimeter_length,perimeter_width):
        self.area_length = area_length
        self.area_width = area_width
        self.perimeter_length = perimeter_length
        self.perimeter_width = perimeter_width

    def area(self):
        area = self.area_length*self.area_width
        print("\nThe area is ",area)
    def perimeter(self):
        perimeter = perimeter_width+perimeter_length
        print("\nThe perimeter is ",perimeter)
    # area calculation
area_length = int(input("\nEnter area (Length): "))
area_width = int(input("\nEnter area (Width): "))
# perimeter calcullation
perimeter_length = int(input("\nEnter perimeter (Length): "))
perimeter_width = int(input("\nEnter width (Width): "))
# conclusion
conclusion = rectangle(area_length,area_width,perimeter_length,perimeter_width)
conclusion.area()
conclusion.perimeter()
