# Accept numbers from user

num = int(input("Enter your number:"))

print("Entered number is ",num)

# Display three strings "name","is","James" as "Name**is**JAmes"

print("Name","is","James",sep="**")  

# Print the octal num of given num

print(oct(num)) 

# display two decimalpoints of a floating number
f_num=34.6876
print(round(f_num,2))

# print all factors of given number

for i in range(1,num+1):
    if num % i == 0:
        print(i,end=" ")

# Accept a list of 5 float num
l1 = []
for i in range(5):
    l1.append(float(input("Enter your no.")))
print(l1)