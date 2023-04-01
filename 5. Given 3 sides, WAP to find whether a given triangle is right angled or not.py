a=int(input("enter first side of triangle:"))
b=int(input("enter second side of triangle:"))
c=int(input("enter third side of triangle:"))
if(a**2==b**2+c**2 or b**2==b**2+a**2 or c**2==b**2+a**2):
    print("triangle is right angled")
else:
    print("triangle is not right angled")    