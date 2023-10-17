# armstrong

n = int(input("Enter your number:"))
num = n
arm = 0
while n > 0:
    arm += (n % 10) ** 3
    n = n//10

if arm == num:
    print(f'Given number {num} is an armstrong no.')
else:
    print(f'Given number is not an armstrong no.')