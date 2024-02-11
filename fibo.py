# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.

# First i print out the first 2 numbers then limit the numbers till 100 using a while loop declared (next) which is
# the value of the last two numbers print it then updates the last two numbers (num1 = num2     num2 = next)

num1 = 0
num2 = 1

print(num1, end=" ")
print(num2, end=" ")

while num1+num2 <=100 :
    next = num1+num2
    print(next, end=" ")
    num1 = num2
    num2 = next
