salary=int(input("salary:"))
age=int(input("age:"))
if(salary >=20000 or age <=25):
    loan=int(input("Enter the loan:"))
    if(loan<=50000):
        print("you are eligible for loan")
    else:
        print("Maximum loan amount is 50000")
else:
    print("you are not eligible")
