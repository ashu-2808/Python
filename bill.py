#Electricity bill calculator using conditional statements and pandas

import pandas as pd
previous_reading=float(input("Enter the previous readimng of the meter:"))
final_reading=float(input("Enter final reading of the meter:"))
final_amount1=0
final_amount2=0
final_amount3=0
uc1=0
uc2=0
uc3=0
if(final_reading>previous_reading):
    units_consumed=final_reading-previous_reading
    if units_consumed<=100:
        final_amount1=units_consumed*2
        uc1=final_reading-previous_reading
    elif units_consumed>100 and units_consumed<=300:
          uc2=final_reading-previous_reading-100
          uc1=100
          final_amount1=uc1*2
          final_amount2=uc2*3
    elif units_consumed>300: 
          uc2=200
          uc1=100
          uc3=final_reading-previous_reading-300
          final_amount1=uc1*2
          final_amount2=uc2*3
          final_amount3=uc3*5
    total_amount=(final_amount1)+(final_amount2)+(final_amount3)
    df=pd.DataFrame({"Slab":["Slab1","Slab2","Slab3","Total:"],"Units Consumed":[uc1,uc2,uc3,uc1+uc2+uc3],"Amount":[final_amount1,final_amount2,final_amount3,total_amount]})
    print(df)
    print("Total Amount to be paid:Rs.",total_amount)
else:
    print("Invalid Input")