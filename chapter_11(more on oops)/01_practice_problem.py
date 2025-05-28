#we have to create a class 2d vector and with the help of this 2d vector we have to show 3d vector as well
class vector_2D:
  i=0
  j=0
  def __init__(self,i,j):
    self.i = i
    self.j = j
  def __add__(self,other):
   return vector_2D(self.i+other.i,self.j+other.j)
  def show(self):
    print(f"{self.i}i + {self.j}j")

class vector_3D(vector_2D):
  k = 0
  def __init__(self,i,j,k):
    self.i = i
    self.j = j 
    self.k = k 
  def show(self):
    print(f"{self.i}i + {self.j}j + {self.k}k")
  def __add__(self,other):
    return vector_3D(self.i+other.i,self.j+other.j,self.k+other.k)

a = vector_3D(1,2,3)
b = vector_3D(4,5,6)
result = a + b
result.show()

