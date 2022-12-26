import random

def Game(b,a):
  if(b==a):
    return None
  elif a==1:
    if(b==3):
      return True
    else:
      return False
  elif a==2:
    if(b==1):
      return True
    else:
      return False
  elif a==3:
    if b==2:
      return True
    else:
      return False
  
print("Computer Turn:-  1} Rock  2} Scissor 3} Paper")
a=random.randint(1,3)

My_Turn=int(input("Enter The Number "))
b=Game(My_Turn,a)

if a==1:
  bot=1
  c="Rock"
elif a==2:
  bot=2
  c="Scissor"
else:
  bot=3
  c="Paper"


if My_Turn==1:
  d="Rock"
elif My_Turn==2:
  d="Scissor"
else:
  d="Paper"

print(f"Computer chooses {c}")
print(f"You chooses {d}")

if b==None:
  print("The Game is Tie")
elif b==True:
  print("You Beat The Computer")
elif b==False:
  print("Computer has beaten you")