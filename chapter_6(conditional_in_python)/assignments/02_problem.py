science_mark = int(input("ENTER THE MARKS OF SCIENCE: "))
sst_marks = int(input("ENTER THE MARKS OF SST: "))
maths_marks = int(input("ENTER THE MARKS OF MATHS: "))
total = science_mark + sst_marks + maths_marks
perscent = (total/300)*100
if(perscent>40 and science_mark > 33 and sst_marks >33 and maths_marks>33):
  print("PASSED!")

else:
  print("failed!")