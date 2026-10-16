# Input we need from the user
#ToTel rent 
#ToTal food ordered for snacking
#Electricity units spend
# charge per unit 
#output
# Total amount you have to pay is 
#prsons living in room?flat
rent= int(input(" enter your flat rent/ hostel rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricty spead = ")) 
charge_per_unit = int(input("Enter  the charge per unit = "))

persons = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend* charge_per_unit

output = (food+rent+total_bill)//persons

print("Each person will pay =", output)
