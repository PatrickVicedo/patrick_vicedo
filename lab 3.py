monthly_salary = float(input("Monthly Salary:"))

if monthly_salary >= 30000:
    print("Eligible")
    loan_amount  = float(input("Loan Amount:"))
    loan = monthly_salary * 10
    if loan_amount <= loan:
        print("Eligible")
        months = int(input("Months:"))
        interest = loan_amount * 0.10
        loan_amount = interest + loan_amount
        payable = loan_amount/months
        print("Total Payment:", loan_amount)
        print("Monthly Payment:",payable) 
    else:
        print("Not Eligible: Loan Request Too High")
else:
    print("Not Eligible: Monthly Salary Too Low")
