try:
  a  = int(input("ENTER FIRST NUMBER: "))
  b = int(input("ENTER SECOND NUMBER: "))
  print(a/b)
except ZeroDivisionError:
  print("infinity")
