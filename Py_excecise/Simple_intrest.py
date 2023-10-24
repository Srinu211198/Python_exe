# WAP to find the simple interest when values of principle rate and time period is given

p = float(input("Principle amount:"))
t = int(input("Time period:"))
r = float(input("rate of interest:"))

si = (p*t*r)/100
print("{} is the simple interest".format(si))

due = p+si

print(f'{due} is the total amount that need to be paid')