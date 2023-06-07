height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

final_output = weight / (height ** 2)
new_final_output = int(final_output)

print(new_final_output)