"""
Write a Python program that:

asks for first name as input (e.g. "James")
asks for last name as input (e.g. "Bond")
Then prints:

"Your name is Bond, James"

Note: The last name is printed first, followed by a comma, and then the first name. 
But if we're using James Bond we'll have to repeat the last mame, yes?
"""
first_name = input("What is your first name please? ")
last_name = input("What is your last name please? ")
full_name = first_name + ' ' + last_name
#print(f"Your name is {last_name}, {full_name}.\nNice to meet you 007.")
print(f"Your name is {last_name}, {full_name}.")
if full_name == "James Bond":
    print("It's nice to meet you 007.")
elif full_name == "Jim Kirk":
    print("Welcome aboard Captain Kirk!")