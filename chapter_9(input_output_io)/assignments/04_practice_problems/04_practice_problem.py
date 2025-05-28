import re

with open("sample.txt","r") as f:
  text = f.read()
  if "donkey" in text.lower():
    text = re.sub(r"donkey","####",text, flags= re.IGNORECASE)

with open("sample2.txt","w") as f:
  f.write(text)
