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
