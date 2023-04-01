a=input("enter the string")
c=len(a)
b=((len(a)-1)//2)-1
print(b)          
print(a[0:b+1])
print(a[c+1:b+3:-1])

if(a[0:b+1]==a[c+1:b+2]):
    print("string is pallidrome")
else:
    print("string is not pallidrome")