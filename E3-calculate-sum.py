"""
Write a Python program to calculate the sum of all numbers in a list. Use a for loop to iterate through each element in the list and add it to a running total.

Example: If the input list is [1, 2, 3, 4], the program should output 10.
"""
MyList = [5, 4, 3, 2, 1]
total = 0
for item in MyList:
    total = total + item
    #print(item)
print("The sum of the items in my list is",total,".")     