amt = int(input("Enter the credit principal:"))
print('''
What do you want to calculate? 
type "m" for the count of months, 
type "p" for monthly payment:
''')
sel = input()
if sel == 'p':
    mon = int(input("Enter the count of months:"))
    if amt % mon == 0:
        print("Your monthly payment = " + str(amt/mon))
    elif amt % mon >= 0.1:
        rem = amt - (int(amt/mon) + 1) * (mon - 1)
        print("Your monthly payment = "+ str((int(amt/mon) + 1)) +" with last month payment = "+ str(rem) +".")
elif sel == 'm':
    pay = int(input("Enter the monthly payment:"))
    if round(amt/pay) == 1:
         print("It takes "+str(round(amt/pay))+" month to repay the credit")
    else:
        print("It takes "+str(round(amt/pay))+" months to repay the credit")


