
first = input("What is your first name? ")
last = input("What is your last name?")
name = first + " " + last
name_length = len(name)
print(name_length)
#print("Hello", name)
print(f"Hello {name}")
print(f"The length of your name is {len(name)}")
if len(name)>10:
    print("Your name is too long")
else:
    print("Your name length is good!")    