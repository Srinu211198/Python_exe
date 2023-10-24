n = int(input("Enter a number"))
r = str(n)[::-1]
print(r)

if int(r) == n:
    print("the given no. is palindrome")
else:
    print("the no. is not palindrome")