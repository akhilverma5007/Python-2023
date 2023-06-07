# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

atmost_age = int(age)
print(atmost_age)
print(type(atmost_age))

total_age = int(90)
years_left = int(total_age) - int(atmost_age)
print("years left ", years_left)
print(type(years_left))

days_left = years_left * int(365)
print("days left ", days_left)
print(type(days_left))

weeks_left = int(days_left/7)
print("Weeks left ",weeks_left)
print(type(weeks_left))

months_left = int(days_left) / 30
months_left_final = int(months_left)
print(months_left_final)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left_final} months left.")

#Write your code below this line 👇