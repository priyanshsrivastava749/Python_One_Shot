import os
old_name = input("Enter the name of file: ")
new_name = input("Enter the new-name of file: ")

try:
  os.rename(old_name,new_name)
except FileNotFoundError:
  print("FILE DOES NOT EXIST!")
except FileExistsError:
  print("File with same name exists: ")
  