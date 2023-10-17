l = input("Enter you number: ")
n = int(l)
rev = 0
'''
# can convert into string and compare easily

rev = l[::-1]
if n == int(rev):
    print("Given number is palindrome")
else:
    print("false")
'''


for i in range(len(l)):
     rev += (n % 10)*(10 ** (len(str(n))-1))
     n = n//10

print(f'The reverse of given no is {rev}')

if int(l) == rev:
    print("True")
else:
    print("False")