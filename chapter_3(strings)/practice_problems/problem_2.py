name = input("Enter name! ")
date = input("Enter date! ")
#we are using f to use variable in the string
letter = f"""Dear {name} 
You are selected!
{date}"""
print(letter)