# narcissist

n = int(input("Enter your number:"))
num = n
nar = 0

while n>0:
    nar += (n%10)**4
    n = n//10

if nar == n:
    print("Given no. is narcissist")
else:
    print(" not an narcissist")