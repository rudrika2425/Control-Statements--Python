import math
print("enter center of circle")
x1=int(input())
y1=int(input())
b=eval(input("enter radius of circle"))
print("enter arbitarary point of circle")
x2=int(input())
y2=int(input())
d=math.sqrt((x1-x2)**2)+((y1-y2)**2)      
if(d>b):
            print("point is outside the circle")
elif(d==b):
            print("point is on the circle")
else:
            print("point is inside the circle")
