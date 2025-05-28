# wap to store the list of fruits entered by users
fruits = []
li = int(input("Enter the number of fruits in the list! "))
index = 0
while index < li :
  fruits.append(input("Enter the fruit name! "))
  index += 1

print(fruits)