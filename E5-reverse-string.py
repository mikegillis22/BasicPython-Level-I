"""
Write a Python program to reverse a string using indices. Use a loop to iterate through each index of the string, starting from the end, and append each character to a new string.

Example: If the input string is "hello", the program should output "olleh".
"""
stringInput = 'We choose to go to the moon!'
stringOutput = ""
x = len(stringInput) - 1
y = 0
for char in stringInput:
   stringOutput += stringInput[x]
   x = x-1
   y = y+1
print(stringInput)   
print(stringOutput)
