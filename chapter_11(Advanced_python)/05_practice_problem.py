n = int(input("ENTER A NUMBER: "))
table = [n*i for i in range(1,11)]
print(table)
with open('table.txt','w') as f:
  f.write(str(table))