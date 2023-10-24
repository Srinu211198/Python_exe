import os
size = os.stat("new_test.txt").st_size

if size == 0:
    print("File is empty")
else:
    print("File is not empty")


with open("new_test.txt","r") as n:
    lines = n.readlines()
    print(lines[3])

with open("new_test.txt","a") as n:
    n.write(input("ener you text"))