def Sum_of_n(n):
  if(n==1):return 1
  return n + Sum_of_n(n-1)

n = int(input("ENTER THE NUMBER: "))
sum = Sum_of_n(n)
print("THE SUM OF FIRST N NATURAL NUMBERS IS: ",sum)