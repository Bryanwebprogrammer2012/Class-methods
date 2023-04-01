print("PAYROLL SYSTEM")

class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name,salary):
        super().__init__(id, name)
        self.salary = salary
       
    def calculate_payroll(self):
        print("\nSalary employee's name : ",self.name,"\n Id : ",self.id,"\n Weekly salary: ",self.salary)
       
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name,salary,commission,):
        super().__init__(id, name,salary)
        self.commission = commission
      

    def calculate_payroll(self):
        formula = self.salary + self.commission
        print("\nCommission employee's name : ",self.name,"\n Id : ",self.id,"\n Weekly salary: ",self.salary,"\nCommission: ",self.commission,"\nTotal: ",formula)

class HourlyEmpoyee(Employee):
    def __init__(self, id, name,hour_rate,hours_worked):
        super().__init__(id, name)
        self.hour_rate = hour_rate
        self.hours_worked = hours_worked
    def calculate_payroll(self):
        salary = self.hour_rate * self.hours_worked
        print("\nHourly employee's name : ",self.name,"\n Id : ",self.id,"\n hours worked:  ",self.hours_worked,"\nHour rate : ",self.hour_rate,"\nSalary: ",salary)


salary = int(input("\nEnter salary for salary employee: "))
e = Employee(1223,"David")
s = SalaryEmployee(1224,"John",salary)
s.calculate_payroll()

salary_commission = int(input("\nEnter salary for commission employee: "))
commission = int(input("\nEnter the commission for commission employee: "))
c = CommissionEmployee(1233,"Bryan",salary_commission,commission)
c.calculate_payroll() 

hour_rate = int(input("\nEnter the hour rate for hourly employee: "))
hours_worked = int(input("\nEnter hours worked for hourly employee: "))
h = HourlyEmpoyee(1244,"Carol",hour_rate,hours_worked)
h.calculate_payroll()

