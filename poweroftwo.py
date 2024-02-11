# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples:
# 8=> returns true
# 6=> returns false

# First collect user input then it checks if the number is positive. if it is positive t continues to check
# if it a power of two using bitwise operation & and if the result is zero it prints true else it prints false
# (example
# (1000 &(1000 - 1)) == 0)
# (1000 &(0111)) == 0
#
# number 8 is 1000 in binary representation
# the result is zero indicating that 8 is a power of two

num = int(input("Enter an integer: "))

if num > 0 and (num & (num - 1)) == 0:
    print(True)
else:
    print(False)
