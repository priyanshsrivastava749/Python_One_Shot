#to print the star pattern
n = int(input("ENTER THE NUMBER OF ROWS: "))
for i in range(1,n+1):
   for j in range(1,i+1):
     print("*",end="")
   print()