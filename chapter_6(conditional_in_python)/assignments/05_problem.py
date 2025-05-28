name_list = ["priyansh","om_jee","piyush","sonu","shashwat"]
flag = False
naam = input("ENTER THE NAME TO BE CHECKED!")
i = 0 
while(i<len(name_list)):
 if(name_list[i] == naam):
      flag = True
      break
 i += 1

if(flag == True):
 print("YES THE NAME IS PRESENT IN THE LIST: ")
else:
 print("No THE name is not present in the list!: ")
