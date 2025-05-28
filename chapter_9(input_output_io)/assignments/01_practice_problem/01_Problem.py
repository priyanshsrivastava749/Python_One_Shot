f = open("first.txt","r")
text = f.read()
if "twinkle" in text:
  print("THE WORD TWINKLE IS PRESENT IN THE POEM!")
f.close()
