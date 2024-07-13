rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
'''
paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''
scissor = '''
  ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''
print(scissor)
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_choice = int(input())
if user_choice == 0:
   print(rock)
elif user_choice == 1:
   print(paper)
elif user_choice == 2:
   print(scissor)
else:
   print("Invalid choice")

print("Computer chose:")
import random
computer_choice = random.randint(0,2)
if computer_choice == 0:
   print(rock)
elif computer_choice == 1:
   print(paper)
elif computer_choice == 2:
   print(scissor)

if (user_choice == 0 and computer_choice == 2):
   print("You win")
elif (user_choice == 2 and computer_choice == 1):
   print("You win")
elif (user_choice == 1 and computer_choice == 0):
   print("You win")
elif (user_choice == computer_choice):
   print("It's a draw")
else:
   print("You lose")


                