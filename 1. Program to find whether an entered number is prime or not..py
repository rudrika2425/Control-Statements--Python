n=int(input("enter the number"))
for i in range(1,n+1):
   if(n%i==0):
      c=+1

if(c>0):
    print("number is not prime")
else:
    print("number is prime")
      
