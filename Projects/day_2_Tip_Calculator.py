print("Welcome to the Day 2 project: the Tip Calculator!\n")
bill_amount = float(input("How much was the bill in dollars? "))
tip_amount = float(input("How much of a tip would you like to give, as a percentage? "))
number_of_people = float(input("How many people to split the bill? "))

tip_percentage = tip_amount / 100
final_amount = bill_amount + (bill_amount * tip_percentage)
per_person_amount = final_amount / number_of_people

print("\n")
print(f"The total amount is: ${round(final_amount, 2)}")
print(f"Each person should pay: ${round(per_person_amount, 2)}")
