x=int(input("Enter first number"))
y=int(input("Enter second number"))
z=int(input("Enter third number"))
if x>y and x>z:
    print(f"{x} is largest")
elif y>x and y>z:
    print(f"{y}is largest")
else :
    print(f"{z} is greatest")