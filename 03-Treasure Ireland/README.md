# Treasure Island Adventure Game

## Introduction
Treasure Island is a simple text-based adventure game where the player's mission is to find the treasure hidden on an island. The game presents the player with a series of choices, each leading to different outcomes, ultimately determining whether the player finds the treasure or faces various challenges along the way.

## Requirements
Python 3.x interpreter

## Implementation

The game is implemented in Python and consists of the following steps:

1. Print the welcome message.
2. Prompt the user for the initial choice: "left" or "right".
3. Based on the user's initial choice:
    - If the user chooses "right", they fall into a hole and the game ends.
    - If the user chooses "left", they reach a lake.
4. If the user chooses to wait at the lake, they arrive at the island unharmed. There, they encounter a house with three doors: red, yellow, and blue.
5. Depending on the door the user chooses:
    - If the user chooses the red door, they encounter a room full of fire and the game ends.
    - If the user chooses the yellow door, they find the treasure and win the game.
    - If the user chooses the blue door, they enter a room of beasts and the game ends.
6. If the user chooses to swim across the lake, they get attacked by an angry trout and the game ends.

The code utilizes Python's `input()` function to collect user input and control flow constructs like `if` statements to handle different scenarios based on the user's choices.

## Description

Treasure Island is a text-based adventure game where players make choices to progress through the story and reach the treasure. The game presents a series of scenarios and prompts the player to make choices, leading to different outcomes based on their decisions.

## ASCII Art

```python
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
```

```python
# Welcome message
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

# Prompt for the initial choice
print('You are at a crossroad. Where do you want to go?\n\tType "left" or "right"')

# User input for the initial choice
user_input1 = input().lower()

# Check the user's initial choice
if user_input1 == "right":
    # Outcome if the user chooses "right"
    print("You fell into a hole. Game Over.")

elif user_input1 == "left":
    # Outcome if the user chooses "left"
    print('You have come to a lake. There is an island in the middle of the lake.\n\tType "wait" to wait for a boat. Type "swim" to swim across.')

    # User input for the second choice
    user_input2 = input().lower()

    # Check the user's second choice
    if user_input2 == "wait":
        # Outcome if the user chooses to wait
        print("You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow, and one blue. Which color do you choose?")

        # User input for the third choice
        user_input3 = input().lower()

        # Check the user's third choice
        if user_input3 == "red":
            # Outcome if the user chooses the red door
            print("It is a room full of fire. Game Over.")
        elif user_input3 == "yellow":
            # Outcome if the user chooses the yellow door
            print("You found the treasure! You Win!")
        elif user_input3 == "blue":
            # Outcome if the user chooses the blue door
            print("You enter a room of beasts. Game Over.")
        else:
            # Outcome if the user enters an invalid input
            print("Invalid Input.")
    
    elif user_input2 == "swim":
        # Outcome if the user chooses to swim
        print("You get attacked by an angry trout. Game Over.")
    else:
        # Outcome if the user enters an invalid input
        print("Invalid Input.")
```


## Output

```
Welcome to Treasure Island.
Your mission is to find the treasure.
You are at a crossroad. Where do you want to go?
    Type "left" or "right"
left
You have come to a lake. There is an island in the middle of the lake.
    Type "wait" to wait for a boat. Type "swim" to swim across.
wait
You arrive at the island unharmed. There is a house with 3 doors.
    One red, one yellow, and one blue. Which color do you choose?
yellow
You found the treasure! You Win!
```
