def pattern1(n):
  if(n==0):return
  for i in range(1,n+1):
    print("*",end="")
  print()
  return pattern1(n-1)

n = int(input("ENTER NUMBER OF ROWS: "))
pattern1(n)