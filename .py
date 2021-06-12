#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator.")
bill=input("What was the total bill?")
tip=input("What percentage tip would you like to give?10,12 or 15?")
bill_in_int=float(bill)
tip_in_int=int(tip)
Tip_div_percentage=tip_in_int/100
Bill_and_tip=bill_in_int*Tip_div_percentage
Total_bill_with_tip=Bill_and_tip+bill_in_int
bill_division=input("How many people to split the bill?")
bill_division_in_int=float(bill_division)
Final_bill_in_float=Total_bill_with_tip/bill_division_in_int
Final_bill=round(Final_bill_in_float,2)
print(f"Each person should pay {Final_bill} ")
