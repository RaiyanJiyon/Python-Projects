# PyPassword Generator

## Description

PyPassword Generator is a Python program that generates a random password based on user-specified criteria, including the number of letters, symbols, and numbers in the password.

## Usage

1. Run the script `password_generator.py`.
2. Follow the prompts to specify the desired number of letters, symbols, and numbers in the password.
3. The program will generate a random password based on the specified criteria and display it to the user.

## Implementation

The program is implemented in Python and consists of the following steps:

1. Initialize lists containing letters, numbers, and symbols.
2. Prompt the user to specify the number of letters, symbols, and numbers in the password.
3. Combine all characters into a single list.
4. Shuffle the combined list to randomize the order of characters.
5. Select characters from the shuffled list to form the password:
   - For letters, symbols, and numbers separately.
6. Shuffle the generated password to further randomize the order.
7. Display the generated password to the user.

The program utilizes Python's `random` module to shuffle characters and select random elements from lists.

## Example

```python
Welcome to the PyPassword Generator!
How many letters would you like in your password?
12
How many symbols would you like?
4
How many numbers would you like?
2
Your password is: q^8T#x%7j$PZnBfA
```

