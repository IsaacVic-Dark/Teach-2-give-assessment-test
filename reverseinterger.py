# Write a program that takes an integer as input and returns an integer with reversed digit
# ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.

# First i collect user input as an integer and checks if it is negative then
# reverses the integer by changing it into a string, reversing the string using
# slicing and convert it back to an integer (reversed_num = int(str(num)[::-1]))
# then if it was negative it multiplies the integer by -1 to make it negative as it was

num = int(input("Enter an integer: "))

negative = False
if num < 0:
    negative = True
    num = abs(num)

reversed_num = int(str(num)[::-1])

if negative:
    reversed_num *= -1

print("Reversed integer:", reversed_num)
