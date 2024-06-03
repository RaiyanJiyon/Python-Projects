import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Combine all characters into a single list
combined_characters = letters + numbers + symbols

# Shuffle the combined list to randomize the order
random.shuffle(combined_characters)

# Select characters from the shuffled list to form the password
password = ""
for _ in range(nr_letters):
    password += random.choice(combined_characters)

for _ in range(nr_symbols):
    password += random.choice(combined_characters)

for _ in range(nr_numbers):
    password += random.choice(combined_characters)

# Shuffle the password to further randomize the order
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print("Your password is:", password)
