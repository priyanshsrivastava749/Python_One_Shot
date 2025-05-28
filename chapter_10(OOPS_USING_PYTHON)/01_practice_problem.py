class programmer:
  def __init__(self,name,role,salary):
    print("You just created an object!")
    self.name = name
    self.role = role
    self.salary = salary
  name = "xyz"
  company = "MICROSOFT"
  role = "python-developer"
  salary = 120000

choice = "y"

while(choice == 'y'):
  name_of_employee = input("ENTER THE NAME OF EMPLOYEE: ")
  role_of_employee = input("ENTER THE ROLE OF EMPLOYEE: ")
  salary_of_employee = input("ENTER TEH SALARY OF EMPLOYEE: ")
  new_object = programmer(name_of_employee,role_of_employee,salary_of_employee)
  choice = input("FOR MORE EMPLOYEE TO ME ADDED PRESS Y: ").lower()
