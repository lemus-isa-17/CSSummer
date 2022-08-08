"""
Isabella Lemus Project 3A

Write a programming solution that will return a value
from the user and return a result based on user input

Get integer (whole number) value from user
Ask them for the amount of US Dollars they want to exchange
for Euros.
For simplicity, euros = dollars * 0.96

Write "if" statement that will give one of two different
outputs.
If it is >= 1,000 dollars,
include the extra dialogue.
If it is < 1,000 dollars, 
keep it simple.
"""

# Prompt user for inputs
print("Enter the amount of US Dollars would you like to exchange")
usd = int(input("for Euros: "))

# Perform calculations
euros = usd * 0.96

if usd >= 1000:
    print('${} is a lot of money to exchange.'.format(usd))
    print('${} US will be {} euros'.format(usd, euros))
else:
    print('${} US is {} euros'.format(usd, euros))
print("Have a nice day!")