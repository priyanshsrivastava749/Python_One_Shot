#WAP TO CONVERT INCHES INTO CMS
def inches_to_cm(inches):
  return inches*2.54

inches = int(input("ENTER LENGTH IN INCHES: "))
cms = inches_to_cm(inches)
print(cms)