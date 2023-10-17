# sum of squares of digits
n = int(input("Enter your number:"))
sum = 0
while n>0:
    sum += (n%10)**2
    n = n//10
print(f'The sum of squares of each digit in given number is {sum}')
