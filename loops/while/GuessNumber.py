secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# You can use triple quotes to print strings on multiple lines in order to make text easier to read, or create a special text-based design.

guess_number = int(input("Guess the number: "))

while guess_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess_number = int(input("Guess the number: "))
    
print("Well done, muggle! You are free now.")
