file1 = input("ENTER A VALID FILE NAME: ")
file2 = input("ENTER ANOTHER VALID FILE NAME: ")
try:
    with open(file1) as f:
      content1 = f.read()
    with open(file2) as f:
      content2 = f.read()
    if content1.lower() == content2.lower():
      print("BOTH FILES ARE IDENTICAL")

except FileNotFoundError:
   print("Please Check the file name agaian: ")