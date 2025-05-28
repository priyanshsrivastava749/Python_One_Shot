class vector:
  def __init__(self,i,j,k):
    self.i = i 
    self.j = j
    self.k = k
  def __str__(self):
    return (f"{self.i}i + {self.j}j + {self.k}k")
  def __add__(self,other):
    return vector(self.i+other.i,self.j+other.j,self.k+other.k)
  def __mul__(self,other):
    return self.i*other.i+self.j*other.j+self.k*other.k
  def __len__(self):
    return 3

a = vector(1,2,3)
b = vector(4,5,6)
print(a)
print(b)
print(a+b)
print(a*b)
print(len(a))