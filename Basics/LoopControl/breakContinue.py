user_input = input("Enter a word: ")

# Ask the user limitlessly
while True:
    if user_input == "chupacabra":
        break; # Break the looponce user enters the secret word
    
    user_input = input("Enter a word: ")
    
# Show this message once user enter the secret word
print("You've successfully left the loop.")
