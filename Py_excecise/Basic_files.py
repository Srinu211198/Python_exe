# with open("file.txt","r") as fp:
#     #reads all thre lines from the file
#     lines = fp.readline()
# print(lines)

#
# try:
#     with open('file.txt', 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found.")

######################################################
# specify the name of the fie you want to create
file_name = "test.txt"

# open the file in  'w' mode to create and write content in it

with open(file_name,'w') as file:
    file.write("line1")
print(f'{file_name}has been create and written into it')

