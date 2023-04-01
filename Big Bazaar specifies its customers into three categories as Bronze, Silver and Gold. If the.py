amount=eval(input())
if (amount>25000):
    print("GOLD")
    print("amount to be paid is:",(20/100)*amount)
elif (amount>10000 and amount<25000):
    print("SILVER")
    print("amount to be paid is:",(10/100)*amount)
else:
    print("BRONZE")
    print("amount to be paid is:",(5/100)*amount)
