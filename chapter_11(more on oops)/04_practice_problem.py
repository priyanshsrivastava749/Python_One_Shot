class complex:
  real = 0
  imaginary = 0
  def __init__(self,real,imaginary):
    self.real = real
    self.imaginary = imaginary
    print(f"{self.real} + {self.imaginary}i")
  def __add__(self,other):
    return complex(self.real+other.real,self.imaginary+other.imaginary)
  def __mul__(self,other):
    return complex(((self.real*other.real)-(self.imaginary*other.imaginary)),((self.real*other.imaginary)+(self.imaginary*other.real)))
  

a = complex(1,2)
b = complex(3,4)
a + b
a * b
