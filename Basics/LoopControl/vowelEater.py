word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word")

for letter in user_word.upper():
    # Complete the body of the loop.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue # continue skips to the condition part of the loop
    
    else:
        word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)
