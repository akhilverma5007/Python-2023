number = int(input("Which number do you want to check? "))

reminder = number % 2
if(reminder != 1):
    print("This is an even number.")
else:
    print("This is an odd number.")