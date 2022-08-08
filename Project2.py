"""

Isabella Lemus Project 2

Design a program that calculates the total shipping charge
required to ship a package based on weight and distance traveled
using the given chart.

Ask user for inputs of weight and zone.

"""

# Prompt user for weight and zone
weight = float(input("Enter package's weight: "))
zone = float(input("Enter the shipping zone: "))

# Calculate cost of shippping
if(weight < 5):
    shippingCost = 5 + zone
elif(weight <= 10):
    shippingCost = 6 + (zone * 2)
else:
    shippingCost = 5 + (zone * 5)

# Print output
print('For a package of weight', weight, 'and zone', zone)
print("The cost of shippping is", shippingCost)
print("Thank you for shipping with us")

"""
When the program outputs the first two print lines it includes the 
(' ','',) parenthesis, quotes, and commas. I was trying to debug but couldn't 
figure out my error...
Suggestions would be great so this doesn't happen next time!
"""