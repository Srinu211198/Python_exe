# WAP to find the volume of cylinder
# cost per ltr mil is 40

r = float(input("Enter the radius :"))
h = float(input("Enter the height :"))

vol = 3.142*(r**2)*h
l = vol/1000 # liters
c = l * 40 # cost

print("Volume of cylinder is ",vol)
print(l," liters of milk is carried by the cylinder")
print("The overall cost of milk is ",c)