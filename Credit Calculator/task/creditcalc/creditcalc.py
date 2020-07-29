import math
print('''
What do you want to calculate? 
type "n" for the count of months, 
type "a" for annuity monthly payment,
type "p" for credit principal:
''')
sel = input()
if sel == 'n':
    P = int(input("Enter credit principal:"))
    A = float(input("Enter monthly payment:"))
    ip = float(input("Enter credit interest:"))
    i = ip / (12 * 100)
    n = math.log(A / (A - i * P), 1 + i)
    if n < 12:
        print("You need "+str(round(n))+" months to repay this credit!")
    elif round(n) % 12 == 0:
        print("You need "+str(round(n / 12))+" years to repay this credit!")
    else:
        print("You need "+str(int(n / 12))+" years and "+str(round(n % 12 + 1))+" months to repay this credit!")


elif sel == 'a':
    P = int(input("Enter credit principal:"))
    n = int(input("Enter count of periods:"))
    ip = float(input("Enter credit interest:"))
    i = ip / (12 * 100)
    A = P * ((i * math.pow(1 + i,n)) / (math.pow(1 + i, n) - 1))
    if A % 10 > 0:
        print("Your annuity payment = "+str(int(A) + 1)+"!")
    else:
        print("Your annuity payment = "+str(round(A))+"!")
elif sel == 'p':
    A = float(input("Enter monthly payment:"))
    n = int(input("Enter count of periods:"))
    ip = float(input("Enter credit interest:"))
    i = ip / (12 * 100)
    P = A / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
    if P % 10 > 0:
        print("Your credit principal = "+str(int(P) + 1)+"!")
    else:
        print("Your credit principal = "+str(round(P))+"!")
else:
    print("Enter a proper value")


