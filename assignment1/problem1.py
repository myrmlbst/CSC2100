# PROBLEM 1

# prompt user to enter values of x & y
x1 = float(input("Enter the value of x1: "))
x2 = float(input("Enter the value of x2: "))
y1 = float(input("Enter the value of y1: "))
y2 = float(input("Enter the value of y2: "))

# calculate the value of m
m = float((y2-y1) / (x2-x1))

# calculate the value of b
b = float(y1 - (m*x1))

# output the results
print("The equation of the line is y = (" + str(m) + ")(x) + " + str(b))