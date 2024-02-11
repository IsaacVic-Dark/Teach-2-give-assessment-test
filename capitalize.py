# Question 4: Capitalize Words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the
# string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

# First i collect user input the program capitalizes the first letter of the word in the sentence
# by checking if the character is a space or beginning of the sentence it capitalizes the next character


word = input("Enter a sentence to capitalize: ")

result_string = ""
capitalize_next = True

for char in word:
    if capitalize_next:
        result_string += char.upper()
        capitalize_next = False
    else:
        result_string += char

    if char == ' ':
        capitalize_next = True
print("Result:", result_string)
