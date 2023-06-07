print("Welcome to the tip calculator.")
Total_bill = input("What was the total bill? $")
print("Total Bill" ,Total_bill)

tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
# print("Tip", tip)

Total_bill_calculated = float(Total_bill) * float(tip) / 100
# print("Total bill afer tip", Total_bill_calculated)

Total_bill_after_tip = float(Total_bill_calculated) + float(Total_bill)
# print("Total bill after tip", Total_bill_after_tip)

split = input("How many people to split the bill? ")
print(int(split))

Final_bill_after_split = float(Total_bill_after_tip) / int(split)


print("Each person should pay: " , Final_bill_after_split)
