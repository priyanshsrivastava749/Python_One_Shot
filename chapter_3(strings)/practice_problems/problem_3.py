# text = "priyansh  is  a  good  boy!"
# index = 0
# while index < len(text):
#    index = text.find("  ",index)
#    if index == -1 :
#       break
#    else: print(f"double space found at index {index}")
#    index += 1

text = "Priyansh  is  a  very  good  boy!"
index = 0
while index<len(text): 
  index = text.find("  ",index) 
  if index == -1:break
  else: print(f"The double space is found at index {index}")
  index += 2
