class employee:
  def __init__(self,salary,increment):
    self.salary = salary
    self.increment = increment
  @property
  def salaryAfterIncrement(self):
    return self.salary + self.salary*self.increment
  @salaryAfterIncrement.setter
  def salaryAfterIncrement(self,new_salary):
    self.increment = (new_salary-self.salary)/self.salary
    self.salary = new_salary
  

a = employee(10000,0.1)
a.salaryAfterIncrement = 12000
print(a.salary)