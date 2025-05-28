# using python programming we have to find out if the number is prime or not
n = int(input("ENTER THE NUMBER: "))
flag = True
for i in range(2,n):
  if(n%i == 0):flag = False

if(flag == False):
  print("THE NUMBER IS NOT PRIME!")
else:
  print("The Number is Prime!")