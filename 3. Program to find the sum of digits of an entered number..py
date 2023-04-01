a=int(input("enter digit:"))
sum=1
while(a!=0 and sum!=0):
  b=a%10 
  sum=sum+b
  a=a/10
print(int(sum))  
