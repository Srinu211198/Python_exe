# print all the factors of a given num provided by user

n = int(input("Enter the number:"))

for i in range(1,n+1):
    if n % i == 0:
        print(i, end=" ")

# accept a list of 5 float num as an input from user
l = []
for _ in range(5):
    l.append(float(input("Enter your number:")))
print(l)