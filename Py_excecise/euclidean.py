import math

x1 = float(input("x1:"))
x2 = float(input("x2:"))
y1 = float(input("y1:"))
y2 = float(input("y2:"))

x = [x1,y1]
y = [x2,y2]

print("Ecludian distance of given points is ",
      round(math.dist(x,y),2))