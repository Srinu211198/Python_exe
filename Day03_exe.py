print("this is about using variable in some math functions");

# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store a complex number
age = 25;
height = 5.8;
c = 3+4j;

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter your base : "))
height = float(input("Enter your height : "))
print("Area of triangle: ", (base*height)/2)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter your 1st side : "))
b = int(input("Enter your 2nd side : "))
c = int(input("Enter your 3rd side : "))
print("the perimeter of the triangle is :",a+b+c)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter your length:"))
width = int(input("Enter your width:"))
print("Area is ",length*width)
print("Parameter is ",2*(length*width))

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input("Enter radius:"))
pi = 3.14
print("Area is ",pi*(r**2))


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = int(input("Enter x-intercept:"))
# y = int(input("Enter y-intercept:"))
y = 2*x-2;
x1,y1=2,2
x2,y2=6,10

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("len(python) compare len(dragon):",len('Python')!=len('dragon'))


