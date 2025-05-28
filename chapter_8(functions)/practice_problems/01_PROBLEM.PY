#wap in python using functions to find greatest of three numbers
def greatest_of_three(a,b,c):
  if(a>b and a>c):
    print(f"{a} is the greatest!")
  elif(b>a and b>c):
    print(f"{b} is the greatest!")
  else:
    print(f"{c} is the greatest!")

a = int(input("ENTER FIRST NUMBER "))
b = int(input("ENTER SECOND NUMBER "))
c = int(input("ENTER THIRD NUMBER "))
greatest_of_three(a,b,c)