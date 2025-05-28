a = int(input("ENTER FIRST NUMBER: "))
b = int(input("ENTER SECOND NUMBER: "))
c = int(input("ENTER THIRD NUMBER: "))
d = int(input("ENTER FORTH NUMBER: "))
if(a>b and a>c and a>d):
  print("FIRST NUMBER IS THE GREATEST!")
elif(b>a and b>c and b>d):
  print("SECOND NUMBER IS THE GREATEST!")
elif(c>b and c>a and c>d):
  print("THIRD NUMBER IS THE GREATEST!")
else:
  print("FORTH NUMBER IS THE GREATEST!")