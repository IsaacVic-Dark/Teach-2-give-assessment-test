# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.
# eg " Hello World " => returns 2

# First you prompt user to enter a sentence then change the sentence to lowercase using .lower() method
# then i created a loop to iterate through each letter to check if it is a vowel
# then if it is a vowel it increments the value of number_of_vowels

sentence =input('Enter your sentence: ').lower()
vowels = 'aeiou'
number_of_vowels = 0

for letter in sentence:
    if letter in vowels:
        number_of_vowels += 1


print("Number of vowels", number_of_vowels)