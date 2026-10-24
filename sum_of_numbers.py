number=int(input("Enter the value of a positive interger:"))
while number<1:
    print("Please enter a positive value.")
    number=int(input("Enter the positive interger"))
total=0
i=1
while i <=number:
    total=total+i
    i=i+1

print(f"The sum of 1 through {number} is {total}")