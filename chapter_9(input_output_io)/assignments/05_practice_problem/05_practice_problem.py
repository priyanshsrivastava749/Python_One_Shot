import re
abusive_words = ["badmash", "chomu", "bhondu", "nalayak", "chutkule", "ullu ka pattha", "gadha", "bewakoof", "faltu"]
sentence = ""
with open("abusive_word.txt","r") as f:
  sentence = f.read()
# now we will use for loop to check for each words presence
flag  = False
for word in abusive_words:
  if word in sentence:
    print(f"'{word}' found in the sentence!")
    flag = True

if flag == True:
  with open("abusive_word_filtered.txt","w") as f:
    for word in abusive_words:
      if word in sentence:
        sentence = re.sub( re.escape(word),"####",sentence,flags = re.IGNORECASE)
    f.write(sentence)
      
    

print("Abusive words censored and written to 'abusive_word_filtered.txt'")