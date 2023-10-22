# accept any three string from one input call

ip = input("Enter the three values with space as seperator: ")

s = ip.split()

print(f'{s[0]} \n{s[1]} \n{s[2]}')