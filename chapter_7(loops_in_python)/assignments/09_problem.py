n = int(input("ENTER THE NUMBER OF LINES: "))
for i in range(1,n+1):
  for j in range(1,4):
    if(i==1 or j==1 or j==3 or i==n):
      print("*",end="")
    else:
      print(" ",end="")
  print()