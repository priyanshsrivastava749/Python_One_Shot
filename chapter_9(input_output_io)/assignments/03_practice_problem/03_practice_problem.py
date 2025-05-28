# import os
# folder_name = "Multiplication_Tables"
# os.makedirs(folder_name,exist_ok = True)
# final_string = ""
# for i in range(2,21):
#  for j in range(1,11):
#   final_string += (f"{i}X{j}={i*j}\n")
#  file_path = os.path.join(folder_name,f"table_{i}.txt")
#  with open(file_path,"w") as f:
#   f.write(final_string)
#  final_string = ""

import os  # OS module import kiya, folder banane aur file path banane ke liye

folder_name = "Multiplication_Tables"  # Folder ka naam jisme tables ki files rakhenge

os.makedirs(folder_name, exist_ok=True)  
# Folder create karenge agar pehle se nahi hai,
# exist_ok=True ka matlab hai agar folder pehle se ho to error nahi aayega

final_string = ""  # Har table ke liye string banani hai, isliye initial empty string

for i in range(2, 21):  # Outer loop for tables 2 se 20 tak

    for j in range(1, 11):  # Inner loop for 1 se 10 tak multiplication
        final_string += (f"{i}X{j}={i*j}\n")  
        # Har step pe line add kar rahe hain string me, jaise "2X1=2"

    file_path = os.path.join(folder_name, f"table_{i}.txt")  
    # File path banaya folder ke andar, file ka naam 'table_2.txt', 'table_3.txt' jaisa

    with open(file_path, "w") as f:  
        f.write(final_string)  
        # File open karke usme poora table (final_string) write kar diya

    final_string = ""  
    # Next table ke liye string ko reset kar diya, taaki pehle ka data na rahe
