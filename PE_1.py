#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

n = int(input("Enter the number:"))
i =1;
sum = 0;
while i < n:
    if (i % 3 == 0 ) | (i % 5 == 0):
        sum = sum + i;
    i +=1;
print(sum);
