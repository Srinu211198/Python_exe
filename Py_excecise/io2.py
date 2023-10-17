# print statement with sepreator

print("name","is","Jhon",sep="**")

# Convert Decimal number to Octal using print()
num = int(input("Enter your number: "))
print(oct(num))

# to remove the octal signs i.e., 0o print last 2 elemets

print(oct(num)[-2:])

# Display float no. with 2 decimals

num = float(input("Enter your number:"))
print(round(num,2))