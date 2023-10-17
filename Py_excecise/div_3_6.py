# WAP that determines the number is div by 3 & 6

n = int(input("Enter your number :"))

if n%3 == 0 and n%6 ==0 :
    print(f'The number {n} is div by 3 & 6')
else:
    print(f'The number {n} is not div by 3 & 6')