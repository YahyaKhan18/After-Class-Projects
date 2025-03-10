x = int(input("Enter first digit : "))
y = int(input("Enter second digit : "))
z = int(input("Enter third digit : "))

num = x*100 + y*10 + z

dig1 = x**3
dig2 = y**3
dig3 = z**3

sum = dig1 + dig2 + dig3

if sum == num:
    print("This is an armstrong number")

else:
    print("This is not an armstrong number")