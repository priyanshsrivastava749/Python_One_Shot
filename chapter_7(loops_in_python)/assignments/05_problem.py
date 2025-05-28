# wap to find sum of first n natural numbers using while loop
n = int(input("ENTER THE NUMBER UP-TILL WHICH YOU WANT TO GET THE SUM OF FIRST N NATURAL NUMBERS: "))
i = 1
sum = 0
while(i<n+1):
  sum+=i
  i+=1

print(sum)