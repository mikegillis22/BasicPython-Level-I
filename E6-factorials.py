"""
Write a Python program to calculate the factorial of a number using a while loop. The factorial of a number is the product of all positive integers up to and including that number.

Example: If the input number is 5, the program should output 120 (which is the product of 5 x 4 x 3 x 2 x 1).
"""
n = 6
numbers = []
z = 0
while n > 0:
    numbers.append(n)
    n = n - 1
print(numbers)
y = len(numbers) - 1
x = numbers[z]
while y > 0:
    z = z + 1
    x = x * numbers[z]
    print(x)
    y = y - 1    
