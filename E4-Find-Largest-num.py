"""
Write a Python program to find the largest number in a list. Use a for loop to iterate through each element in the list and keep track of the largest element seen so far

Example: If the input list is [1, 5, 3, 8, 2], the program should output 8.
"""
MyList = [3, 22, 9, 72, 12, 1]
LargestNum = 0
for number in MyList:
    if LargestNum < number:
        LargestNum = number
print("The largest number in my list is",LargestNum,".")

