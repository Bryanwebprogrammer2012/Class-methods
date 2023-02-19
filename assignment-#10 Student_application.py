class student:
    def __init__(self,name,rollnumber):
        self.name = name
        self.rollnumber = rollnumber
    # displaying student's information
    def display(self):
        display = print("Student's name ",name,"\n Student's roll number ",rollnumber)
        print(display)
    # randomly giving the student his/her age from 18 - 60
    def set_age(self):
        import random
        age = random.randrange(18,60) 
        print("Student's age ",age)
    # randomly giving the student marks from 1 - 100
    def set_marks(self):
        import random
        marks = random.randrange(1,100)
        print("Student's marks ",marks)

name = input("Student's name:  ")
rollnumber = int(input("\nStudent's roll number: "))
student_application = student(name,rollnumber)
student_application.display()
student_application.set_age()
student_application.set_marks()
