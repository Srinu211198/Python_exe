# print all the factors of given number

n = int(input("Enter your number:"))

for i in range(1,n+1):
    if n % i == 0:
        print(i,end=" ")
