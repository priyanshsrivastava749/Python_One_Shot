#calculate the factorial of a given number
n = int(input("Enter the number: "))
factorial = 1
for i in range(1,n+1):
  factorial *= i

print(factorial)