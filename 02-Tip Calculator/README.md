# Tip Calculator

## Description

This script calculates the total bill amount including tip and splits it among a specified number of people.

## Usage

1. Run the script `tip_calculator.py`.
2. Enter the total bill amount when prompted.
3. Enter the tip percentage you would like to give.
4. Enter the number of people to split the bill among.

## Code

```python
# Printing the welcome message
print("Welcome to the tip calculator!")

# Taking the total bill amount as input from the user
total_bill = float(input("What was the total bill? $"))  

# Taking the tip percentage as input from the user
tip_percentage = int(input("What percentage tip would you like to give? "))  

# Taking the number of people to split the bill as input from the user
split_people = int(input("How many people to split the bill? "))  

# Calculating the tip amount based on the total bill and tip percentage
tip_amount = total_bill * (tip_percentage / 100)

# Calculating the total bill amount including the tip
total_bill_with_tip = total_bill + tip_amount

# Calculating the amount each person should pay after splitting the bill
split_bill = total_bill_with_tip / split_people

# Formatting the final amount to two decimal places
final_amount = "{:.2f}".format(split_bill)

# Printing the amount each person should pay
print(f"Each person should pay: ${final_amount}")
```
## Example

```
Welcome to the tip calculator!
What was the total bill? $100
What percentage tip would you like to give? 15
How many people to split the bill? 4
Each person should pay: $28.75
```
