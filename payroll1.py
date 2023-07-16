class Employee:
    def __init__(self,id,name):
     self.id=id
     self.name=name
class SalaryEmployee(Employee):
    def __init__(self,id,name,basicsalary,allowance):
      self.basicsalary = basicsalary
      self.allowance= allowance
      super().__init__(id,name)
    def calculate_basicsalary(self):
        salary=self.basicsalary + self.allowance
        print("Basic salary:")
        print("ID:", self.id)
        print("Name:", self.name)
        print("salary:", salary)
        return

class HourlyEmployee(Employee):
    def __init__(self, id, name, hoursworked,hourlypay):
      self.hoursworked = hoursworked
      self.hourlypay=hourlypay
      super().__init__(id, name)

    def calculate_hourlypay(self):
        hourlypayroll=self.hourlypay * self.hoursworked
        print("Hourly salary:", self.hourlypaya)
        print("ID:",self.id)
        print("Name:", self.name)
        print("Hourly payroll:", hourlypayroll)
        return


class CommissionEmployee(SalaryEmployee):
    def __init__(self,id,name,commissionrate,basicsalary,allowance):
        self.commissionrate= commissionrate
        super().__init__(id, name, basicsalary, allowance)

    def calculate_commission(self):
        commission=(self.basicsalary + self.allowance) * self.commissionrate
        print("Commission rate:", self.commissionrate)
        print("ID:", self.id)
        print("Name:", self.name)
        print("Commission:", commission)
        return

id=input("Enter ID:")
name=input("Enter name:")
basicsalary=float(input("Enter Basic Salary:"))
allowance=float(input("Enter Allowance:"))
hourlypay=float(input("Enter Hourly Pay:"))
hoursworked=float(input("Enter Hours Worked:"))
commissionrate=float(input("Enter Commission Rate:"))


Employeedetails1 = HourlyEmployee(id, name, hoursworked, hourlypay)
Employeedetails1.calculate_hourlypay()

Employeedetails2 = SalaryEmployee(id, name, basicsalary, allowance)
Employeedetails2.calculate_basicsalary()

Employeedetails3 = CommissionEmployee(id, name, basicsalary, allowance, commissionrate)
Employeedetails3.calculate_commission()

