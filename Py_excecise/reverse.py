# WAP to extract each digit from an integer in the reverse order

n = int(input("Enter the number:"))

y = str(n)[::-1]

print(f'The reverse of given number is : {int(y)}')