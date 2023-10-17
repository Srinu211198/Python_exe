# Program to find the sum of digits

l = input("Enter you number :")
n = int(l)
sum = 0;

for i in range(len(l)):
     sum += n % 10
     n = n // 10
print(sum)