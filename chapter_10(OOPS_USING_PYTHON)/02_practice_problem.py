class Calculator: 
  def __init__(self,num): #basically ye ek constructor hai jo ki ek number ko set kar deta hai is class k liye
    self.num = num

  def square_root(self,num):
    return self.num ** (1/2)
  
  def cube_root(self,num):
    return self.num ** (1/3)
  
num = float(input("ENTER THE NUMBER: "))
new_object = Calculator(num)
print(f"SQUARE ROOT OF {num}: {new_object.square_root(num)}")
print(f"CUBE ROOT OF {num}: {new_object.cube_root(num)}")