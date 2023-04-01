num=int(input("enter the number"))
for i in range (num):
   size = len(str(i))
   hold = i
   sum = 0
while(hold>0):
        digit = hold % 10
        sum += digit**size
        hold //= 10
if(sum==i):
   print(i)
   i = i + 1

