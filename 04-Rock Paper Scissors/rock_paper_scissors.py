rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

user_input = int(input())
computer_input = random.randint(0, 2)

if user_input == computer_input:
    if user_input == 0 and computer_input == 0:
        print("Your Input - " + str(user_input))
        print(rock)
        print("Computer Input - " + str(computer_input))
        print(rock)
        print("Draw")
    elif user_input == 1 and computer_input == 1:
        print("Your Input - " + str(user_input))
        print(paper)
        print("Computer Input - " + str(computer_input))
        print(paper)
        print("Draw")
    else:
        print("Your Input - " + str(user_input))
        print(scissors)
        print("Computer Input - " + str(computer_input))
        print(scissors)
        print("Draw")
    

elif user_input == 0 and computer_input == 1:
    print("Your Input - " + str(user_input))
    print(rock)
    print("Computer Input - " + str(computer_input))
    print(paper)
    print("Paper covers Rock. Computer wins!")

elif user_input == 0 and computer_input == 2:
    print("Your Input - " + str(user_input))
    print(rock)
    print("Computer Input - " + str(computer_input))
    print(scissors)
    print("Rock crushes Scissors. You win!")

elif user_input == 1 and computer_input == 0:
    print("Your Input - " + str(user_input))
    print(paper)
    print("Computer Input - " + str(computer_input))
    print(rock)
    print("Paper covers Rock. You win!")

elif user_input == 1 and computer_input == 2:
    print("Your Input - " + str(user_input))
    print(paper)
    print("Computer Input - " + str(computer_input))
    print(scissors)
    print("Scissors cut Paper. Computer wins!")

elif user_input == 2 and computer_input == 0:
    print("Your Input - " + str(user_input))
    print(scissors)
    print("Computer Input - " + str(computer_input))
    print(rock)
    print("Rock crushes Scissors. Computer wins!")

elif user_input == 2 and computer_input == 1:
    print("Your Input - " + str(user_input))
    print(scissors)
    print("Computer Input - " + str(computer_input))
    print(paper)
    print("Scissors cut Paper. You win!")

else:
    print("Invalid input. Please choose 0 for Rock, 1 for Paper, or 2 for Scissors.")
