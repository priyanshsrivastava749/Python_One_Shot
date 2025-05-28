# write a program to accept marks of 6 students and display them in a sorted manner
marks = []
li = int(input("ENTER THE NUMBER OF STUDENTS!: "))
i = 0
while i<li: 
 marks.append(int(input(f"ENTER THE MARKS OF {i+1} student: ")))
 i += 1

marks.sort()
print(marks)