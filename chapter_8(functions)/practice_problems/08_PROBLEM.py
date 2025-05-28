# def table(n):
#   for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")
#   return

def table(n,i):
  if(i == 0):return
  table(n,i-1)
  print(f"{n} X {i} = {n*i}")
  return

n = int(input("ENTER THE NUMBER: "))
table(n,10)