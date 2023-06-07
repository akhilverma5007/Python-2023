# Nested if statement
# height = int(input("Please enter your height in cm "))
# age = int(input("Please enter your age"))

# if(height > 120):
#     print("Can ride")
#     if(age > 18):
#         print("Over 18 and have to pay $12")
#     else:
#         print("Under 18 and have to pay #7")
# else:
#     print("Can't ride")


# Elif statement
height1 = (int(input("Please enter your height ")))

if height1 >= 120:
    print("You can ride")

    age1 = (int(input("Please enter your age ")))
    if age1 < 12:
        print("Under 12 and have to pay $5")
    elif age1 < 12 & age1 > 18:
        print("Between 12 to 18 and have to pay $7")
    else:
        print("Over 18 and have to pay $12")

else:
    print("Can't ride")