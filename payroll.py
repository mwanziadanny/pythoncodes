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

    def calculate_hourlypayrol(self):
        hourlypayroll=self.hourlypay* self.hoursworked
        print("Hourly salary:", self.hourlypay)
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



Employeedetails1 = HourlyEmployee(23, 'midy', 56, 3500)
Employeedetails1.calculate_hourlypayrol()

Employeedetails2 = SalaryEmployee(23, 'midy', 230000, 5700)
Employeedetails2.calculate_basicsalary()

Employeedetails3 = CommissionEmployee(23, 'midy', 230000, 5700, 0.17)
Employeedetails3.calculate_commission()

