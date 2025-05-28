import random

def game(score):
  #rock paper scissor
  your_choice = input("ENTER YOUR CHOICE 'stone' 'paper' 'scissors': ")
  computer_selection = random.randint(0,2)
  computer_choice = ""
  
  if(computer_selection == 0):
    computer_choice = "stone"
  elif(computer_selection == 1):
    computer_choice = "paper"
  else:
    computer_choice = "scissors"
  choice_list = {
    "stone":0,
    "paper":1,
    "scissors":2
  }
  choice_list_reverse = {
    0:"stone",
    1:"paper",
    2:"scissors"
  }
  if your_choice not in choice_list:
    print("INVALID CHOICE!")
    return score
  if(choice_list[your_choice] == choice_list[computer_choice]):
    print(f"YOUR CHOICE IS {your_choice} And COMPUETERS CHOICE IS {computer_choice}")
    print("ITS A DRAW!")
  else:
    if(choice_list[your_choice] == 0 and choice_list[computer_choice] == 1):
      print(f"YOUR CHOICE IS {your_choice} And COMPUETERS CHOICE IS {computer_choice}")
      print("YOU LOSE!")
    elif(choice_list[your_choice] == 0 and choice_list[computer_choice] == 2):
      print(f"YOUR CHOICE IS {your_choice} And COMPUETERS CHOICE IS {computer_choice}")
      print("YOU WIN!")
      score +=1

    elif(choice_list[your_choice] == 1 and choice_list[computer_choice] == 0):
      print(f"YOUR CHOICE IS {your_choice} And COMPUETERS CHOICE IS {computer_choice}")
      print("YOU WIN!")
      score +=1

    elif(choice_list[your_choice] == 1 and choice_list[computer_choice] == 2):
      print(f"YOUR CHOICE IS {your_choice} And COMPUETERS CHOICE IS {computer_choice}")
      print("YOU LOSE!")
    elif(choice_list[your_choice] == 2 and choice_list[computer_choice] == 0):
      print(f"YOUR CHOICE IS {your_choice} And COMPUETERS CHOICE IS {computer_choice}")
      print("YOU LOSE!")
    elif(choice_list[your_choice] == 2 and choice_list[computer_choice] == 1):
      print(f"YOUR CHOICE IS {your_choice} And COMPUETERS CHOICE IS {computer_choice}")
      print("YOU WIN!")     
      score +=1

  return score

choice = "y"
current_score = 0
try:
    f = open("hiscore.txt","r")
    hi_score = int(f.read())
    f.close()
except FileNotFoundError:
  f = open("hiscore.txt","w")
  f.write("0")
  f.close()
  hi_score = 0

while choice.lower() == 'y':
  current_score = game(current_score)
  choice = input("Enter Your choice press 'Y' or 'Y' for more rounds: ")

if current_score > hi_score :
  print(f"CURRENT-SCORE IS {current_score} AND HIGH SCORE IS {hi_score}")
  f = open("hiscore.txt","w")
  f.write(str(current_score))
  f.close()
  print(f"NEW HIGH SCORE IS {current_score}")


