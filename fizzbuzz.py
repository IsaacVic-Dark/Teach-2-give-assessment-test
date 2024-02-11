# Question 1: FizzBuzz
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
# multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
# "FizzBuzz".

# First i created a for loop to limit the numbers to 100 then an if statement to see if the number is a
# multiple of both 5 and 3 (if num % 5 == 0 and num % 3 == 0:) then check for multiples of 3 the 5.

for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz", end=" ")
    elif num % 3 == 0:
        print("Fizz", end=" ")
    elif num % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(num, end=" ")

