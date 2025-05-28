f = open("second.txt","r")
txt = f.read()
if "twinkle" in txt.lower(): 
  print("YES THE WORD TWINKLE IS PRESENT IN THE POEM!")
else :
  print("NO THE WORD TWINKLE IS NOT PRESENT IN THE POEM!")