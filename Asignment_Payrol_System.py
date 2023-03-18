class Employee:
    def __init__(self,employee_1,employee_2,employee_3):
        self.employee_1 = employee_1
        self.employee_2 = employee_2
        self.employee_3 = employee_3

    def carol_employee(self,salary_carol):
        def calculate_payrol():
            print("Carol's salary ",salary_carol)

    def jenny_employee(self,salary_jenny):
        def calculate_payrol():
            print("Jenny's salary ",salary_jenny)

    def john_employee(self,salary_john):
        def calculate_payrol():
            print("John's  salary ",salary_john)


class SalaryEmployee(Employee):
    def weekly_salary(weekly_salary_carol,weekly_salary_jenny,weekly_salary_john):
        def carol_weekly_salary():
            print("Carol's weekly salary ",weekly_salary_carol)

        def jenny_employee():
            print("Jenny's weekly salary ",weekly_salary_jenny)

        def john_employee():
            print("John's weekly salary ",weekly_salary_john)

class HourlyEmpoyee:
    def __init__(self,hourly_employee_1,hourly_empoyee_2,hourly_empoyee_3,):
       self.hourly_employee_1 = hourly_employee_1
       self.hourly_empoyee_2  = hourly_empoyee_2
       self.hourly_empoyee_3 = hourly_empoyee_3
    
    def calculate_payrol(amount_for_an_hour):
        hours_worked_employee_1 = 5
        hours_worked_employee_2 = 6
        hours_worked_employee_3 = 7
        def payroll():
            employee_1_payroll = hours_worked_employee_1 * amount_for_an_hour
            employee_2_payroll = hours_worked_employee_2 * amount_for_an_hour
            employee_3_payroll = hours_worked_employee_3 * amount_for_an_hour
            print("David's hourly payroll: ",employee_1_payroll)
            print("Samuel's hourly payroll: ",employee_2_payroll)
            print("Bryan's hourly payroll: ",employee_3_payroll)

class CommissionEmployee(SalaryEmployee):
    def __init__(self, commission, fixed_salary):
        self.commission = commission
        self.fixed_salary = fixed_salary
    def calculate_payroll(self):
        CFV = self.commission + self.fixed_salary


employee_1 = "Carol",12233
employee_2 = "Jenny",444422
employee_3 = "John",555551

conclusion_employee = Employee(employee_1,employee_2,employee_3)
conclusion_employee.carol_employee(20000)
conclusion_employee.jenny_employee(25000)
conclusion_employee.john_employee(30000)

conclusion_salary_employee = SalaryEmployee()
conclusion_salary_employee.weekly_salary(5000,6250,7500)

hourly_empoyee_1 = "David",14444
hourly_empoyee_2 = "Samuel",224444
hourly_empoyee_3 = "Bryan",3334444

conclusion_hourly_employee = HourlyEmpoyee(hourly_empoyee_1,hourly_empoyee_2,hourly_empoyee_3)
conclusion_hourly_employee.calculate_payrol(5000)

conclusion_commission_employee = CommissionEmployee(5500,25000)
