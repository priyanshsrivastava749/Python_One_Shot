class Calculator:
  def __init__(self,num):
    self.num = num
  def square_root(self,num):
    return self.num ** (1/2)
  def cube_root(self,num):
    return self.num ** (1/3)
  @staticmethod
  def greeting():
    print("HELLO USER!")  

num = float(input("ENTER THE NUMBER: "))
new_object = Calculator(num)
print(new_object.square_root(num))
print(new_object.cube_root(num))
new_object.greeting()