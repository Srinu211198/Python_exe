# Swap the number without using 3rd variable

a = int(input("Enter you 1st number:"))
b = int(input("Enter you 2nd number:"))
#
# # using +,-
# a = a+b
# b = a-b
# a = a-b

# using *,/
a = a*b
b = a/b
a = a/b
print(f'The values after swapping are a = {a}, b = {b}')


