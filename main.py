# File: main.py
# Description: Program will prompt User for a temperature in Celsius, convert the temperature to Fahrenheit, and print the result.
# Author: Jessica Priester
# Email: jessicp0249@student.vvc.edu
# Created: 10 Sep 2019

# Get temperature in Celsius from user
temp_C = float(input('Enter temperature in Celsius:\n'))

# Print converted temperature
print('%0.2f degrees Fahrenheit' % (temp_C * 9 / 5 + 32))
