'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''

height = float(input("Please enter your height: "))
weight = float(input("Please enter your weight: "))

final = weight / (height ** 2)
final_output = int(final)
if weight > 18.5:
    print(f"Your bmi is: {final_output} and you're underweight")
elif weight < 18.5 & weight >= 25:
    print(f"Your bmi is: {final_output} and you have normal weight") 
elif weight < 25 & weight > 30:
    print(f"Your bmi is: {final_output} and you're slightly overweight")
elif weight < 30 & weight > 35:
    print(f"Your bmi is: {final_output} and you're obese")
elif weight > 35:
    print(f"Your bmi is: {final_output} and you're clinically obese")


