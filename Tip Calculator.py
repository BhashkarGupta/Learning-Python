print("welcome to the tip calculator.")
bill = float(input("What was the total bill?\n$ "))
tip_percentage = float(input("What percentage tip would you like to give?\n")) / 100
people = int(input("How many people to split the bill?\n"))
# print(f"Each person should pay: ${round(((bill * tip_percentage ) + bill) / people, 2)}")
payment = round(((bill * tip_percentage ) + bill) / people, 2)
final_payment = "{:.2f}".format(payment) # strictly to two decimal
print(f"Each person should pay: ${final_payment}")
