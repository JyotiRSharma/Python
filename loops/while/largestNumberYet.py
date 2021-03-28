largest_number = -9999

#Accept first number
num = int(input("Enter a number or press -1 to exit: "))

# Find the largest among the number until user presses -1
while num != -1:
        # Check if the current input is the largest
        if num > largest_number:
                largest_number = num

        # Ask the user again and again
        num = int(input("Enter a number or press -1 to exit: "))

print(largest_number)
