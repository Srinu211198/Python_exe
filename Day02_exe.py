first_name = "Harry"
last_name = "Potter"
age = 21    
Country = 'England'
city = 'London'
Capital_city= "London"
is_marries = True
hobbies = ('rides', 'pets','someother things')

skills = ['Magic Spells','Can talk with snakes','Cursed',hobbies]
Contacts = {'Caretaker1' : 'Hagrid',
            'Caretaker2' : 'Dumble Door',
            'secret_caretaker' : hobbies}

friends = {('ron','Harmony'),('malfboy','wesley')}

# Check the data type of all your variables using type() built-in function
print(type(first_name))

# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name
print(len(first_name),len(last_name))

# Declare 5 as num_one and 4 as num_two
num_one = 5;
num_two = 4;

# Add num_one and num_two and assign the value to a variable total
total = num_one+num_two

# Subtract num_two from num_one and assign the value to a variable diff
num_two -= num_one

# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

# Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# The radius of a circle is 30 meters.
r = 30

# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * (r*r)

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circumference_of_circle = 2*3.14*r

# Take radius as user input and calculate the area.
radius = int(input("Enter your radius:"))
area = 3.14*(radius*radius)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
age = input("Enter your age:")    
Country = input("Enter your country name:")

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('Keywords')
