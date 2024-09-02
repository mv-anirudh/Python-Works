loan_amount=float(input("enter your loan amount : "))

annual_interest_rate=float(input("enter your annual interest rate: "))
loan_tenure=float(input("enter the tenure : "))

tenure=loan_tenure*12

monthly_interest_rate=(annual_interest_rate / 100) / 12

emi=loan_amount * monthly_interest_rate * (1 + monthly_interest_rate)**tenure/((1+monthly_interest_rate)**tenure-1)

print(f"the monthly emi is {emi}")

total_pay=emi*tenure

print(f"total payable={total_pay}")

total_interest_pay= total_pay-loan_amount
print(f"total payabel interest={total_interest_pay }")