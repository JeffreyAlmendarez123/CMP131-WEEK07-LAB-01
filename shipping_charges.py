#Jeffrey Alemndarez
#cmp131
#week7
#LAB1
#SHIpping_charges.py
#10/9/26


weight=float(input("Enter the weight for the package (kg):"))
while weight <= 0 or weight > 20:
    print("Weight must be more than 0 and no more than 20 kg.")
    weight=float(input("Enter the weight of the package (kg):"))
#Getting our weight information and getting the input from the user

distance=float(input("Enter the distance to shipout(miles)"))
while distance <10 or distance >3000:
    print("Distance must be in the range of 10-3,000 miles.")
    distance=float(input("Enter the distance for it to be shipped (miles):"))

    
    
if weight <=2:
        rate = 1.10
elif weight<=6:
        rate = 2.20
elif weight<=10:
     rate= 3.70
else:
     rate= 4.80

charges=(distance / 500) * rate
print(f"Rate: ${rate:.2f}")
print(f"Shipping charged: ${charges:.2f}" )  