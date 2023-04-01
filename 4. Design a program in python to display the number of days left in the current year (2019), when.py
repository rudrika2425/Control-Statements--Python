date=eval(input("enter date:"))
month=input("enter month :")
if month=="january":
    days=31
    left=334
elif month=="february":
    days=28
    left=306
elif month=="march":
    days=31
elif month=="april":
     days=30
     left=245
elif month=="may":
     days=31
     left=214
elif month=="june":
      days=30
      left=184
elif month=="july":
      days=31
      left=153
elif month=="august":
      days=31
      left=122
elif month=="september":
      days=30
      left=92
elif month=="october":
      days=31
      left=61
elif month=="november":
      days=30
      left=31
elif month=="december":
      days=31
      left=0
              
              
              
days_left_in_that_month= (days-date)+left
print("the number of days left are:",days_left_in_that_month)
