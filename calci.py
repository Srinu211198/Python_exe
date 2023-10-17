num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))

opr = (input("Enter your operator : "))


def calci(num1,num2,opr):
    if opr == '+':
        print("Your sum is :", num1+num2)
    elif opr == '-':
        print("Your sub is :", num1-num2)
    elif opr == '*':
        print("Your mul is :", num1*num2)
    else:
        print("Invalid operator")

r = calci(num1,num2,opr)




