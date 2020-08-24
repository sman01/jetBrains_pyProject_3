
import argparse
import math
import sys

parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=float)
parser.add_argument('--payment', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

credit_principal = args.principal
monthly_payment = args.payment
periods_number = args.periods
credit_interest = args.interest
type_user = args.type

if len(sys.argv) < 4:
    print("Incorrect parameters")

elif type_user != "annuity" and type_user != "diff":
    print("Incorrect parameters")

elif type_user == "diff" and monthly_payment is not None:
    print("Incorrect parameters")

elif credit_interest is None:
    print("Incorrect parameters")

elif type_user == "annuity":

    if periods_number is None:

        nominal_interest_rate = credit_interest / (12 * 100)

        periods_number = round(
            math.log((monthly_payment / (monthly_payment - (nominal_interest_rate * credit_principal))),
                     (1 + nominal_interest_rate)) + 0.5)

        years = periods_number // 12

        months = periods_number % 12

        if years == 1 and months == 0:
            print("You need " + str(years) + " year to repay this credit!")
        elif years > 1 and months == 0:
            print("You need " + str(years) + " years to repay this credit!")
        elif years == 0 and months == 1:
            print("You need " + str(months) + " month to repay this credit!")
        elif years == 0 and months > 1:
            print("You need " + str(months) + " months to repay this credit!")
        elif years == 1 and months == 1:
            print("You need " + str(years) + " year and " + str(months) + " month to repay this credit!")
        elif years == 1 and months > 1:
            print("You need " + str(years) + " year and " + str(months) + " months to repay this credit!")
        elif years > 1 and months == 1:
            print("You need " + str(years) + " years and " + str(months) + " month to repay this credit!")
        elif years > 1 and months > 1:
            print("You need " + str(years) + " years and " + str(months) + " months to repay this credit!")

    elif monthly_payment is None:

        nominal_interest_rate = credit_interest / (12 * 100)
        monthly_payment = round(credit_principal * ((
                nominal_interest_rate * math.pow((1 + nominal_interest_rate), periods_number) / (
                math.pow((1 + nominal_interest_rate), periods_number) - 1))) + 0.5)
        print("Your annuity payment = " + str(monthly_payment) + "!")

    elif credit_principal is None:

        nominal_interest_rate = credit_interest / (12 * 100)
        credit_principal = round(monthly_payment / (
                (nominal_interest_rate * math.pow((1 + nominal_interest_rate), periods_number)) / (
                math.pow((1 + nominal_interest_rate), periods_number) - 1)))
        print("Your credit principal = " + str(credit_principal) + "!")

    total = periods_number * monthly_payment

    print("\nOverpayment = " + str(round(total - credit_principal)))

elif type_user == "diff":

    nominal_interest_rate = credit_interest / (12 * 100)

    total = 0

    for m in range(1, int(periods_number) + 1):
        diff_payment = round((credit_principal / periods_number) + nominal_interest_rate * (
                credit_principal - ((credit_principal * (m - 1)) / periods_number)) + 0.5)
        print("Month " + str(m) + ": paid out " + str(diff_payment))
        total += diff_payment

    print("Overpayment = " + str(round(total - credit_principal)))
