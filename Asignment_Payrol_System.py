print("PAYROLL SYSTEM")

class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)
       
    def calculate_payroll(self):
        weekly_salary = 20000
        print("\nSalary employee's name : ",self.name,"\n Id : ",self.id,"\n Weekly salary: ",weekly_salary)
       
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name):
        super().__init__(id, name)
      

    def calculate_payroll(self):
        commission = 34444
        print("\nCommission employee's name : ",self.name,"\n Id : ",self.id,"\n Weekly salary: ",commission)

class HourlyEmpoyee(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)
       

    def calculate_payroll(self):
        hour = 5
        hour_rate = hour * 5000
        print("\nHourly employee's name : ",self.name,"\n Id : ",self.id,"\n Weekly salary: ",hour_rate)

e = Employee(1223,"David")
s = SalaryEmployee(1224,"John")
s.calculate_payroll()

c = CommissionEmployee(1233,"Bryan")
c.calculate_payroll() 

h = HourlyEmpoyee(1244,"Carol")
h.calculate_payroll()

