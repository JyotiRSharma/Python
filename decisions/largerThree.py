# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Assume umber to be the largest
largest_number = number1

# Check if the largest number is number2
# and update
if number2 > largest_number:
    largest_number = number2

# Check if the largest number is number3 and then update
if number3 > largest_number:
    largest_number = number3
    
# Print the result
print("The largest number is:", largest_number)    
