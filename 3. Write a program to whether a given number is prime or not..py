num=eval(input("enter the number :"))
count=0
for i in range(2,num):
    if(num%i==0):
        count+=1
    else:
        count==0  
if(count>0):
    print("number is not prime")
else:
    print("number is prime")              
    