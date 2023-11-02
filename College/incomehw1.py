income=int(input("Enter your annual income: "))
if income<500000: 
    tax=0
    print("No tax taken, you have: ", income)
elif income==500000: 
    tax = (5/100)*income
    income = income-tax
    print("5% tax taken, you have: ", income)
elif income>=1000000 and income<=1500000: 
    tax=(10/100)*income
    income=income-tax
    print("10% tax taken, you have: ", income)
elif income>1500000:
    tax=(30/100)*income
    income=income-tax
    print("30% tax taken, you have: ", income)

